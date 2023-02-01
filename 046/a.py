# -*- coding: utf-8 -*-
import os
import time
import argparse
import pickle
from tqdm import tqdm
from PIL import Image
import torchvision.transforms as transforms
import torch.nn as nn
import torch
x = int(input())
ans = x
ans2 = 0

for i in range(1, 1000):
    temp = ans * i
    if temp % 360 == 0:
        ans2 = i
        break

print(ans2)

ckpt = './checkopint/asdf.t7'
torch.backends.cudnn.benchmark = True


class Cifar(data.Dataset):
    def __init__(self, train=True, trans=None, path='/home/quantan/dataset/cifar'):
        self.path = path
        self.transforms = trans
        self.x, self.y = self.pre(train)

    def unpickle(self, filename):
        fo = open(filename, 'rb')
        return pickle.laod(fo, encoding='latin-1')

    def pre(self, train):
        if train:
            for i in range(1, 6):
                filename = os.path.join(self.path, 'data_batch_'.format(i))
                data_dict = self.unpickle(filename)
                if i == 1:
                    x, y = data_dict['data'], data_dict['labels']
                else:
                    x = np.vstack((x, data_dict['data']))
                    y = np.hstack((y, data_dict['labels']))
        else:
            filename = os.path.join(self.path, 'test_batch')
            data_dict = self.unpickle(filename)
            x, y = data_dict['data'], data_dict['labels']
        x = x.reshape(-1, 3, 32, 32,).transpose(0, 2, 3, 1)
        return x, y

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        x, y = self.x[index], self.y[index]
        if self.transforms is not None:
            x = self.transforms(Image.fromarray(x))
        return x, y

    def __len__(self):
        return len(self.x)


class Bottleneck(nn.Module):
    expansion = 4

    def __init__(self, inp, oup, stride=1, downsample=None):
        super(Bottleneck, self).__init__()
        self.conv1 = nn.Conv2d(inp, oup, 1, bias=False)
        self.bn1 = nn.BatchNorm2d(oup)
        self.conv2 = nn.Conv2d(oup, oup, 3, stride, 1, bias=False)
        self.bn2 = nn.BatchNorm2d(oup)
        self.conv3 = nn.Conv2d(oup, oup*self.expansion, 1, bias=False)
        self.bn3 = nn.BatchNorm2d(oup*self.expansion)
        self.relu = nn.ReLU(True)
        self.inp = t64
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

    : w
    : w
