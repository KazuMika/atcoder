N = int(input())

T = []
ti = 0
xi = 0
yi = 0
flag = True
# t+1に点(x+1,y),(x−1,y),(x,y+1),(x,y−1)の
for i in range(N):
    T.append(list(map(int, input().split())))


for t, x, y in T:
    dift = t - ti
    difx = x - xi
    dify = y - yi
    dif = difx + dify
    ti = t
    xi = x
    yi = y
    if dift % dif == 0:
        continue
    else:
        flag = False
        break


if flag:
    print("Yes")
else:
    print("No")
