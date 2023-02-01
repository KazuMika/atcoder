n, m, k = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
ans = [0]
time_sum = 0
i, j = 0, 0

flag_a = True
flag_b = True
flag = False
for i in range(0, len(aa)+1):
    for j in range(0, len(bb)+1):
        asum, bsum = sum(aa[:i]), sum(bb[:j])
        if k < asum and k < bsum:
            flag = True
            break
        else:
            time_total = asum + bsum
            if time_total > k:
                break
            else:
                ans.append(i+j)
    if flag:
        break

print(max(ans))
