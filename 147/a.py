# -*- coding: utf-8 -*-
a = map(int, input().split())
if sum(a) <= 21:
    print('win')
else:
    print('bust')


