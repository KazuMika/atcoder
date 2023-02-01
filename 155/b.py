n = int(input())
A = list(map(int, input().split()))

for a in A:
    if a % 2 == 0 and (a % 5 != 0 and a % 3 != 0):
        print("DENIED")
        exit(0)


print('APPROVED')
