n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
ans = 0
for i in range(len(arr)):
    ans += arr[i] * (n-i-1) - arr[i] * i
print(ans)
