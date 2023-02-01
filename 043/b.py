ss = input()
ans = []

for s in ss:
    if s == '0':
        ans.append('0')
    elif s == '1':
        ans.append('1')
    elif s == 'B' and len(ans) != 0:
        ans.pop()

print(''.join(ans))
