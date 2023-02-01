N, K = map(int, input().split())
d = set()
A = set()

for i in range(K):
    d.add(input())
    for i in list(map(int, input().split())):
        A.add(i)

print(N-len(A))
