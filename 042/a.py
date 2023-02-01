s = map(int, input().split())
target = 17

for i in s:
    if (i == 5 or i == 7):
        target = target - i

print(target)
if target == 0:
    print("YES")
else:
    print("NO")
