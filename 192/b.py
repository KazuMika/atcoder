
s = input()
ans = True

for i in range(len(s)):
    if i % 2 == 0 and s[i].isupper():
        ans = False
    elif i % 2 == 1 and s[i].islower():
        ans = False


if ans:
    print('Yes')
else:
    print('No')
