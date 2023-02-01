from itertools import permutations
import math

n = int(input())

cs = []

def get_dis(c, c2):
    x = c[0]-c2[0]
    y = c[1]-c2[1]
    return math.sqrt(x*x+y*y)


for i in range(n):
    cs.append(list(map(int, input().split())))


dis = 0
c = 0
for citeis in permutations(cs, n):
    c += 1
    for i in range(len(citeis)-1):
        dis += get_dis(citeis[i], citeis[i+1])

print(dis/c)
