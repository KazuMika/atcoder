n, m = map(int, input().split())
sc = []
for i in range(m):
    sc.append(list(map(int, input().split())))


for i in range(10**n):
    s = str(i)
    if len(s) == n and all([s[sc[j][0]-1] == str(sc[j][1]) for j in range(m)]):
        print(s)
        exit(0)


print('-1')


#
# for i in range(1, n+1):
#    if list(zip(*sc))[0].count(i) > 1:
#        print('-1')
#        exit(0)
#
#
# if min(list(zip(*sc))[0]) != 1:
#    print('-1')
#    exit(0)
#
# for i in sc:
#    if i[0] == 1 and i[1] == 0 and n > 1:
#        print('-1')
#        exit(0)
#
#ans = [0, 0, 0]
# for i in sc:
#    ind, val = i[0]-1, i[1]
#    if ans[ind] != 0:
#        ans[ind] = min(ans[ind], val)
#    else:
#        ans[ind] = val
#
#print(''.join(list(map(str, ans))))
