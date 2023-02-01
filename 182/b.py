n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(2, 1000):
    temp = 0
    for j in range(len(a)):
        if a[j] % i == 0:
            temp += 1
    if ans <= temp:
        ans = temp
        ansi = i
print(ansi)
