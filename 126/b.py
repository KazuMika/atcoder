x = input()
a, b = int(x[0:2]), int(x[2:4])
flag = 0
ans = ["AMBIGUOUS", "YYMM", "MMYY", "NA"]

if (a >= 1 and a <= 12) and (b >= 1 and b <= 12):
    flag = 0
elif (a == 0 and b > 12) or (b == 0 and a > 12) or (b > 12 and a > 12) or (b == 0 and a == 0):
    flag = 3
elif ((a > 0 and a <= 12) and (b >= 13)) or (b == 0 and (a >= 1 and a <= 12)):
    flag = 2
elif ((a >= 13) and (b > 0 and b <= 12)) or (a == 0 and (b >= 1 and b <= 12)):
    flag = 1


print(ans[flag])
