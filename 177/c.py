n = int(input())
a = list(map(int, input().split()))

sums = 0
for i in range(n-1):
    for j in range(i+1, n):
        sums += (a[i] * a[j])

print(sums % (10 ** 9 + 7))
