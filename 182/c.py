from itertools import permutations as perm
n = int(input())
if n % 3 == 0:
    print(0)
    exit(0)
else:
    ans = 0
    n = list(str(n))
    for i in range(1, len(n)):
        for v in perm(n, i):
            temp = n.copy()
            for q in v:
                temp.pop(temp.index(q))
            num = int(''.join(temp))
            if num % 3 == 0:
                print(i)
                exit(0)


print(-1)
