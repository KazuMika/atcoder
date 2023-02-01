n = int(input())
s = [input() for _ in range(n)]
ans = set()

for i in s:
    ans.add(i)

print(len(ans))
