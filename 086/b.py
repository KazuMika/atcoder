a, b = input().split()
ans = int(a+b)
i = 2
flag = False
while (i**2) < 100100:
    if (i**2) == ans:
        flag = True
        break

    i += 1

if flag:
    print("Yes")
else:
    print("No")
