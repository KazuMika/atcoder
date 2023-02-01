nums = tuple(map(int, input().split()))
s = set(nums)
if len(s) == 2:
    print('Yes')
else:
    print("No")
