k = int(input())
a, b = map(int, input().split())
flag = True

#
# while i < b:
#    if k == 1:
#        flag = True
#        break
#    dis = i * k
#    if dis >= a and dis <= b:
#        flag = True
#        break
#
#    i += 1

for i in range(a, b):
    if i % k == 0:
        print("OK")
        flag = False
        break


if flag:
    print("NG")
