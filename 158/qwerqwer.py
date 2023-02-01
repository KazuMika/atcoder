# -*- coding: utf-8 -*-
import torch
import torch.nn as nn
import torch.utils.data as data
import pickle
import argparse
import time
import os
from PIL import Image
from tqdm import tqdm
import numpy as np
import torchvision.transforms as transforms

ckpt = './checkpoint/asdf.t7'
torch.backends.cudnn.benchmark = True

class Cifar(data.Dataset):
    def __init__(self, train=True, trans=None, path='/Users/quantan/sample/cifar'):
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
            filename = os.path.join(self.at)
