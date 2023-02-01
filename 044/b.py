s = input()
acsii = [chr(i) for i in range(97, 97+26)]
flag = True
for i in acsii:
    if s.count(i) % 2 != 0:
        flag = False
        break

if flag:
    print('Yes')
else:
    print("No")
