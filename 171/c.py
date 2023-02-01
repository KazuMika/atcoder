n = int(input())
ans = []
asc = 'zabcdefghijklmnopqrstuvwxy'
a = 0
i = 1
while n >= a:
    a += 26**i
    i += 1

for j in range(1, i-1):
    n -= 26 ** j


while n > 0:
    s = (n % 26)
    ans.append(s)
    n = int(n / 26)

ans2 = []
for i in ans:
    ans2.append(asc[i])

test = ''.join(ans2)
print(test)
