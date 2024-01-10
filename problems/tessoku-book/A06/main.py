#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from heapq import heappop, heappush
from itertools import permutations, combinations, combinations_with_replacement, product
from collections import defaultdict, Counter
import fractions
import bisect
import sys

sys.setrecursionlimit(10000)


def slover():
    N, Q = get_arr()
    A = get_arr()
    A = [0] + A
    for i in range(1, len(A)):
        A[i] += A[i-1]

    for i in range(Q):
        l, r = get_arr()
        ans = A[r] - A[l-1]
        print(ans)


def get_n():
    return int(input())


def get_arr():
    return list(map(int, input().split()))


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

    def size(self, x):
        return -self.pare[self.find(x)]

    def roots(self):
        return [i for i in range(self.n) if self.pare[i] < 0]


class Sort(object):
    def __init__(self, n):
        self.n = n

    def sort(self, nums):
        if len(nums) == 0:
            return []

        left, eq, right = [], [], []
        pivot = nums[len(nums) // 2]

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                eq.append(num)
            else:
                right.append(num)

        left = self.sort(left)
        right = self.sort(right)
        return left + eq + right


def gcd_and_lcm():
    # 最大公約数、最小公倍数
    a, b = map(int, input().split())
    f = fractions.gcd(a, b)
    f2 = a * b // f
    print(f, f2)

    # combinations、組み合わせ、順列
    a = ['a', 'b', 'C']
    print(list(permutations(a)))
    print(list(combinations(a, 2)))
    print(list(combinations_with_replacement(a, 3)))

    # ビット演算、式を計算
    a = list(product(['+', '-'], repeat=3))
    s = ['5', '5', '3', '4']
    for i in a:
        ans = s[0] + i[0] + s[1] + i[1] + s[2] + i[2] + s[3]
        if eval(ans) == 7:
            print(ans + '=7')
            break

    # 集計
    a = [2, 2, 2, 3, 4, 3, 1, 2, 1, 3, 1, 2, 1, 2, 2, 1, 2, 1]
    a = Counter(a)
    for i in a.most_common(3):
        print(i)

    # n進数
    n = 64
    k = -3
    bi = ''
    while n != 0:
        bi += str(n % abs(k))
        if k < 0:
            n = -(-n // k)
        else:
            n = n // k
    print(bi[::-1])


# 二部探索
def binominal_search():
    a = [1, 2, 3, 5, 6, 7, 8, 9]
    b = bisect.bisect_left(a, 8)


def spp():
    # 最短経路
    ys, xs = 2, 2
    yg, xg = 4, 5
    a = ['########', '#......#', '#.######', '#..#...#', '#..##..#', '##.....#', '########']
    n = [(ys - 1, xs - 1)]
    route = {n[0]: 0}
    p = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    count = 1
    while route.get((yg - 1, xg - 1), 0) == 0 and count != 10000:
        n2 = []
        for i in n:
            for j in p:
                ns = (i[0] + j[0], i[1] + j[1])
                if a[ns[0]][ns[1]] == '.' and route.get(ns, -1) == -1:
                    n2.append(ns)
                    route[ns] = count
        n = n2
        count += 1
    print(n, route)


def dfs():
    # 深さ探索
    q = [{1, 3}, {1, 4}, {9, 5}, {5, 2}, {6, 5}, {3, 5}, {8, 9}, {7, 9}]
    count = 0
    while count != 10000:
        a = q.pop()
        for j in q:
            if len(j & a) != 0:
                j |= a
                count = 0
                break
        else:
            q = [a] + q
        if count > len(q):
            break
        count += 1
        print(count, q)


def main_bfs():
    # 幅優先探索
    n = 7
    pt = [[1, 2, 3], [0], [5, 0], [6, 0], [6], [2], [3, 4]]

    def bfs(v):
        d = [-1] * n
        d[v] = 0
        q = [v]
        c = 1
        while q:
            q1 = []
            for i in q:
                for j in pt[i]:
                    if d[j] == -1:
                        d[j] = c
                        q1.append(j)
            q = q1
            c += 1
            print(d, q)
        return d

    print(bfs(0))


if __name__ == "__main__":
    slover()
