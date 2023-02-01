n = int(input())
ho = int(str(n)[-1])

if ho in [2, 4, 5, 7, 9]:
    print('hon')
elif ho in [0, 1, 6, 8]:
    print('pon')
else:
    print("bon")
