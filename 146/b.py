n = int(input())
s = input()
#al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#ans = ""
#
# for i in s:
#    ind = al.index(i) + n
#    ans += al[ind % 26]
# print(ans)
ans = ''
for i in s:
    ans += chr((ord(i)-65+n) % 26 + 65)

print(ans)
