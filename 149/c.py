# -*- coding: utf-8 -*-
import math
x = int(input())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False


while is_prime(x):
    x += 1

print(x)
