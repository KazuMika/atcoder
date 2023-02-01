x = int(input())
money = 100
i = 0

while True:
    i += 1
    money = int(money * 1.01)
    if money >= x:
        break

print(i)
