n = int(input())

A = []  # x,y xの人がusotki
for i in range(n):
    a = int(input())
    temp = []
    for k in range(a):
        x, y = map(int, input().split())
        temp.append([x, y])
    A.append(temp)


s1 = set()
s2 = set()

for x, y in A:
    if y == 1:
        s1.add(x)
    else:
        s2.add(x)

print(s1, s2)
print(n-len(s2))
