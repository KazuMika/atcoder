n, k = map(int, input().split())
s = list(input())

temp = s[k-1]
if temp == "A":
    s[k-1] = "a"
elif temp == "B":
    s[k-1] = "b"
else:
    s[k-1] = "c"

print(''.join(s))
