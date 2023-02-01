N, K = map(int, input().split())

pre = N
curr = N

for i in range(K):
    sorted_num = sorted(str(pre))
    g1 = int(''.join(reversed(sorted_num)))
    g2 = int(''.join(sorted_num))
    curr = g1 - g2
    pre = curr


print(curr)
