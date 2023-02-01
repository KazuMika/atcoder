n = int(input())

while n > 0:
    mod = n % 10
    if mod == 7:
        print('Yes')
        exit(0)
    n = n / 10

print('No')
