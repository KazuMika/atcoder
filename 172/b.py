ss = input()
tt = input()
ans = 0

for s, t in zip(ss, tt):
    if s != t:
        ans += 1
print(ans)
