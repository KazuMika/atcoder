# -*- coding: utf-8 -*-

import argparse
import numpy as np
import time
from collections import defaultdict
import os
import pickle
from PIL import Image
from tqdm import tqdm
import unittest
from urllib import request, error
import torch
from torch import nn, optim, cuda
from torchvision import transforms
import tarfile
from pathlib import Path
from torch.utils.data import Dataset, DataLoader


URL = 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
EXT_DIR = 'cifar-10-batches-py'


def make_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cuda", action='store_true', default=True)
    parser.add_argument("--resume", action='store_true')
    parser.add_argument("--epoch", type=int, default=100)
    parser.add_argument("--ckpt", type=str, default=None)
    parser.add_argument("--cifar_dir", default=None)
    parser.add_argument("--output_dir", default='ckpt')
    args = parser.parse_args()
    args.device = torch.device('cuda' if args.cuda and cuda.is_available() else 'cpu')
    return args


class Cifar(Dataset):
    def __init__(self, train=True, trans=None, path='./cifar'):
        self.path = Path(path)
        self.transforms = trans
        self.path.mkdir(parents=True, exist_ok=True)

        if len(list(self.path.iterdir)) == 0:
            self.download(self.path)

        self.x, self.y = self.pre(train)

    def unpickle(self, filename):
        with open(filename, 'rb') as fo:
            return pickle.load(fo, encoding='latin-1')

    def pre(self, train):
        if train:
            for i in range(1, 6):
                filename = self.path / f"data_batch_{i}"
                data_dict = self.unpickle(filename)
                if i == 1:
                    x, y = data_dict['data'], data_dict['labels']
                else:
                    x = np.vstack((x, data_dict['data']))
                    y = np.hstack((y, data_dict['labels']))
        else:
            filename = self.path / 'test_batch'
            data_dict = self.unpickle(filename)
            x, y = data_dict['data'], data_dict['labels']
        x = x.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
        return x, y

    def __getitem__(self, index):
        x, y = self.x[index], self.y[index]
        if self.transforms is not None:
            x = self.transforms(Image.fromarray(x))
        return x, y

    def __len__(self):
        return len(self.x)

    def download(self, cifar_dir):
        try:
            tar_file = URL.split('/')[-1]

            with request.urlopen(URL) as web, open(tar_file, 'wb') as fo:
                fo.write(web.read())
            with tarfile.open(tar_file) as tar:
                tar.extractall()
            os.rename(EXT_DIR, cifar_dir)
        except error.URLError as e:
            print(e)


class Bottleneck(nn.Module):
    expansion = 4

    def __init__(self, inp, oup, stride=1, downsample=None):
        super(Bottleneck, self).__init__()
        self.conv1 = nn.Conv2d(inp, oup, 1, bias=False)
        self.bn1 = nn.BatchNorm2d(oup)
        self.conv2 = nn.Conv2d(oup, oup, 3, stride, 1, bias=False)
        self.bn2 = nn.BatchNorm2d(oup)
        self.conv3 = nn.Conv2d(oup, oup * self.expansion, 1, bias=False)
        self.bn3 = nn.BatchNorm2d(oup * self.expansion)
        self.relu = nn.ReLU(True)
        self.downsample = downsample

    def forward(self, inp):
        out = self.relu(self.bn1(self.conv1(inp)))
        out = self.relu(self.bn2(self.conv2(out)))
        out = self.bn3(self.conv3(out))
        residual = inp
        if self.downsample is not None:
            residual = self.downsample(inp)
        out += residual
        out = self.relu(out)

        return out


class ResNet(nn.Module):
    def __init__(self, block, blocks, class_num=10):
        super(ResNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, 7, 2, 3, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(True)
        self.inp = 64
        self.layer1 = self._make_layer(block, 64, blocks[0], 1)
        self.layer2 = self._make_layer(block, 128, blocks[1], 2)
        self.layer3 = self._make_layer(block, 256, blocks[2], 2)
        self.layer4 = self._make_layer(block, 512, blocks[3], 2)
        self.avg = nn.AvgPool2d(2, 1)
        self.linear = nn.Linear(512 * block.expansion, class_num)

    def forward(self, inp):
        out = self.relu(self.bn1(self.conv1(inp)))
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = self.avg(out)
        out = out.view(out.size(0), -1)
        out = self.linear(out)
        return out

    def _make_layer(self, block, oup, blocks, stride=1):
        layers = []
        downsample = None
        if stride != 1 or self.inp != oup * block.expansion:
            downsample = nn.Sequential(
                nn.Conv2d(self.inp, oup * block.expansion, 1, stride, bias=False),
                nn.BatchNorm2d(oup * block.expansion)
            )
        layers.append(block(self.inp, oup, stride, downsample))
        self.inp = oup * block.expansion
        for i in range(blocks):
            layers.append(block(self.inp, oup))

        return nn.Sequential(*layers)


class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.pare = [-1] * n

    def find(self, x):
        if self.pare[x] < 0:
            return x
        else:
            self.pare[x] = self.find(self.pare[x])
            return self.pare[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if x > y:
            x, y = y, x

        self.pare[x] += self.pare[y]
        self.pare[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i in range(self.n) if self.pare[i] < 0]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root or i == root]

    def groups(self):
        dic = defaultdict(list)
        rs = self.root()
        for r in rs:
            dic[r] = self.members(r)

        return dic


class Trainer(object):
    def __init__(self, args):
        self.args = args
