a, b, c, k = map(int, input().split())

for i in range(3):
    if i == 0:
        if k <= a:
            print(k)
            break
        else:
            k -= a

    elif i == 1:
        if k <= b:
            print(a)
            break
        else:
            k -= b

    elif i == 2:
        if k <= c:
            print(a+(-1*k))
        else:
            print(a+c)
