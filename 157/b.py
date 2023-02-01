a = [list(map(int, input().split())) for i in range(3)]
#a = []
# for i in range(3):
#    temp = list(map(int, input().split()))
#    a.extend(temp)
n = int(input())
b = [int(input()) for _ in range(n)]
ans = []

for i in b:
    for index, cow in enumerate(a):
        for index2, k in enumerate(cow):
            if i == k:
                a[index][index2] = True

for i in a:
    if i.count(True) == 3:
        print('Yes')
        exit(0)


for i in zip(*a):
    if i.count(True) == 3:
        print("Yes")
        exit(0)


temp = [a[i][i] for i in range(3)]
temp2 = [a[i][2-i] for i in range(3)]
if temp.count(True) == 3 or temp2.count(True) == 3:
    print('Yes')
    exit(0)


print('No')
