N, M = map(int, input().split())
H = list(map(int, input().split()))
ans = M
counted = []
appeared = set()


for i in range(M):
    a, b = map(int, input().split())
    if H[a-1] < H[b-1]:
        appeared.add(a)
    elif H[a-1] > H[b-1]:
        appeared.add(b)
    else:
        appeared.add(a)
        appeared.add(b)

ans = len(H) - len(appeared)
print(ans)
