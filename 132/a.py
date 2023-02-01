s = input()
counter = {}
flag = True

for i in s:
    if i not in counter:
        counter[i] = 1
    else:
        counter[i] += 1

for x, y in counter.items():
    if y != 2:
        flag = False
        break

if flag:
    print('Yes')
else:
    print("No")
