n, k = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse=True)
H = H[k:]
print(sum(H))
