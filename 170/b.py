x, y = map(int, input().split())
flag = False

for i in range(x+1):
    ans = (i*2)+((x-i)*4)
    if ans == y:
        flag = True


if flag:
    print('Yes')
else:
    print("No")
