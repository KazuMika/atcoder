a, b, x = map(int, input().split())
l, r = 1, x
while l <= r:
    mid = (l+r)//2
    ans = a * mid + b * (len(str(mid)))
    if ans > x:
        r = mid-1
    elif ans < x:
        l = mid+1
    else:
        if mid > 10**9:
            print(10**9)
        else:
            print(mid)
        exit(0)

if l > 10**9:
    print(10**9)
else:
    print(l-1)
