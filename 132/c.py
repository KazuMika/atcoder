import numpy as np
n = int(input())
ds = list(map(int, input().split()))
ds = np.array(ds)
ans = 0
bs = 1
for i in range(max(ds)):
    temp1 = np.count_nonzero(ds < i)
    temp2 = np.count_nonzero(ds >= i)
    if temp1 == temp2:
        ans += 1

print(ans)
