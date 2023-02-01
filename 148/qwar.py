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


ckpt = './checkpoint/asdf.t7'
torch.backends.cudnn.benchmark = True

class Cifar(data.Dataset):
    def __init__(self, train=True, trans=None, path='/Users/quantan/sample/cifar'):
        self.path = path
        self.transforms = trans
        self.x, self.y = self.pre(train)

    def unpickle(self, filename):
        f = open(filename, 'rb')
        return pickle.load(fo, encoding='latin-1')

    def pre(self, train):
