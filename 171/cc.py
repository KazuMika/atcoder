n = int(input())
s = 1
i = 0
asc = 'zabcdefghijklmnopqrstuvwxy'
ans = []


# a=1,aa=27,aaa = 26 + 26*26+1
while n > s:
    s += 26 ** i
    i += 1

keta = i-1
temp = n - (s/26)

while temp > 0:
    t = (temp % 26)
    ans.append(t)
    temp = int(temp / 26)

ans2 = []
for i in ans:
    ans2.append(asc[i])

test = ''.join(ans2)
print(test)
