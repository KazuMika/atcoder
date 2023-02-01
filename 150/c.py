import itertools
n = int(input())
p = input().replace(' ', '')
q = input().replace(' ', '')
s = itertools.permutations(list(range(1, n+1)), n)
pi = 0
qi = 0
for i, sb in enumerate(s):
    sb = ''.join(map(str, sb))
    if sb == p:
        pi = i
    if sb == q:
        qi = i

print(abs(pi-qi))
