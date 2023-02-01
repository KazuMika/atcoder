n = int(input())
div = n % 10

if div in [2, 4, 5, 7, 9]:
    print('hon')
elif div in [0, 1, 6, 8]:
    print('pon')
else:
    print('bon')
