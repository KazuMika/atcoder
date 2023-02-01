n = int(input())
ls = list(map(int, input().split()))
ans = 0
san = []

for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        for k in range(j+1, len(ls)):
            temp1 = ls[i] != ls[j] and ls[j] != ls[k] and ls[i] != ls[k]
            temp2 = ls[i] + ls[j] > ls[k] > abs(ls[i]-ls[j])
            temp3 = ls[j] + ls[k] > ls[i] > abs(ls[j]-ls[k])
            temp4 = ls[i] + ls[k] > ls[j] > abs(ls[i]-ls[k])
            if temp1 and (temp2 or temp3 or temp4):
                san.append([ls[i], ls[j], ls[k]])

                ans += 1

print(ans)
