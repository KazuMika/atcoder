n, k = map(int, input().split())
nums = []
ans = 0
for i in range(1, n+1):
    temp = i
    counter = 0
    while k > temp:
        temp *= 2
        counter += 1

    ans += 1/n * (1/2)**counter
print(ans)
