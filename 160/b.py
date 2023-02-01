x = int(input())

c_500 = x // 500
r_500 = x % 500
c_5 = r_500 // 5

print(c_500 * 1000 + c_5 * 5)
