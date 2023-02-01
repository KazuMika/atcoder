s = input()
target = s[:(len(s)-1)//2]
target2 = s[(len(s)+3)//2-1:]
if target == target2:
    l, r = 0, len(s)-1
    flag = True
    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            print('No')
            exit(0)

    print("Yes")


else:
    print('No')
