h, n = map(int, input().split())
A = list(map(int, input().split()))

if h <= sum(A):
    print("Yes")
else:
    print("No")
