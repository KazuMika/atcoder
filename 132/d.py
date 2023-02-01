# -*- coding: utf-8 -*-
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import pickle
import argparse
import time
import os
from PIL import Image
from tqdm import tqdm
import numpy as np
import torch.utils.data as data


ckpt = './checkpoint/asdf.t7'
torch.backends.cudnn.benchmark = True


class Cifar(data.Dataset):
    def __init__(self, train=True, trans=None, path='/Users/quantan/sample/data'):
        self.path = path
        self.transforms = trans
        self.x, self.y = self.pre(train)

    def unpickle(self, filename):
        fo = open(filename, 'rb')
        return pickle.load(fo, encoding='latin-1')

    def pre(self, train):
        if train:
            for i in range(1, 6):
                filename = os.path.join(self.path, 'data_batch_{}'.format(i))
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
        x = x.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
        return x, y

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        x, y = self.x[index], self.y[index]
        if self.transforms is not None:
            x = self.trnasforms(Image.fromarray(x))
        return x, y


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
        self.downsample = downsample
        self.inp = 64

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
        self.conv1 = nn.Conv2d(3, 64, 7, 2, 3, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.inp = 64
        self.relu = nn.ReLU(True)
        self.layer1 = self._make_layer()
        self.layer2 = self._make_layer(block, 128, blocks[1], 2)
        self.layer3 = self._make_layer(block, 256, blocks[2], 2)
        self.layer4 = self._make_layer(block, 512, blocks[3], 2)
        self.avg = nn.AvgPool2d(2, 1)
        self.linear = nn.Linear(512*block.expansion, class_num)

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
                nn.Conv2d(self.inp, oup*block.expansion,
                          1, stride, bias=False),
                nn.BatchNorm2(oup*block.expansion)

            )

        layers.append(block(self.inp, oup, stride, downsample))
        self.inp = oup * block.expansion
        for i in range(blocks):
            layers.append(block(self.inp, oup))

        return nn.Sequential(*layers)


class Trainer(object):
    def __init__(self, args):
        self.args = args
        self.net = ResNet(Bottleneck, [2, 2, 2, 2], 10).to(self.args.device)
        if self.args.resume:
            ck = torch.load(ckpt)
            self.lr = ck['lr']
            self.best_acc = ck['acc']
            self.start_epoch = ck['epoch']
            self.net.load_state_dict(ck['net'])
        else:
            self.lr = 0.01
            self.start_epch = 0
            self.start_epoch = 0

        trans = {
            'train':
                transforms.Compose([
                    transforms.RandomCrop(32, 4),
                    transforms.RandomHorizontalFlip(),
                    transforms.ToTensor(),
                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                ]),
                'test':
                transforms.Compose([
                    transforms.ToTensor(),
                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                ])
        }

        train, test = Cifar(True, trans['train']), Cifar(False, trans['test'])
        self.trainloader = data.DataLoader(train, 128, True)
        self.testloader = data.DataLoader(test, 128, False)
        self.optimizer = torch.optim.SGD(
            self.net.parameters(), self.lr, 0.9, weight_decay=5e-4)
        self.criterion = nn.CrossEntropyLoss()

    def adjust_learning_rate(self):
        self.lr = self.lr * 0.1
        for i in self.optimizer.param_groups:
            i['lr'] = self.lr
        print(self.lr)

    def training(self, epoch):
        losses, correct = 0, 0
        self.net.train()
        if epoch % 100 == 0:
            self.adjust_learning_rate()

        for x, y in tqdm(self.trainloader):
            x, y = x.to(self.args.device), y.to(self.args.device)
            output = self.net(x)
            loss = self.criterion(output, y)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            losses += loss.item()
            correct += output.max(1)[1].eq(y).sum().item()
        losses /= len(self.trainloader)
        acc = 100.0 * correct / len(self.trainloader.dataset)
        print('losses:{0:0.3f}. acc{1:0.3f}.'.format(losses, acc))

    def validation(self, epoch):
        losses, correct = 0, 0
        self.net.eval()
        for x, y in self.testloader:
            x, y = x.to(self.args.device), y.to(self.args.device)
            output = self.net(x)
            losses += self.criterion(output, y).item()
            correct += output.max(1)[1].eq(y).sum().item()
        losses /= len(self.testloader)
        acc = 100. * correct / len(self.testloader.dataset)
        print('losses:{0:0.3f}. acc{1:0.3f}.'.format(losses, acc))
        if self.best_acc < acc:
            print('savint')
            state = {
                'net': self.net.state_dict(),
                'lr': self.lr,
                'epoch': epoch,
                'acc': acc
            }
            torch.save(state, ckpt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--cuda", action='store_true')
    parser.add_argument("--resume", action='store_true')
    args = parser.parse_args()
    args.device = torch.device(
        "cuda" if args.cuda and torch.cuda.is_available() else 'cpu')
    trainer = Trainer(args)
    start_epoch = trainer.start_epoch
    total_time = 0
    for epoch in range(start_epoch+1, start_epoch+300):
        print('epoch:{}'.format(epoch))
        t = time.time()
        trainer.training(epoch)
        trainer.validation(epoch)
        t = time.time()-t
        print('end_time:{}'.format(int(t)))
        total_time += t
        print('total_time:{}'.format(int(total_time)))
    print('end_training')
