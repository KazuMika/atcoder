
k = int(input())

if k % 2 == 0 or k % 5 == 0:
    print(-1)
else:
    n = 7
    cnt = 1
    for i in range(k):
        if n % k == 0:
            break
        cnt += 1
        n = (n * 10 + 7) % k
    print(cnt)
