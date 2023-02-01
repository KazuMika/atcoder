def main():
    n, k = input().split()
    ds = list(map(int, input().split()))
    p_num = list(set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(ds))
    p_num.sort()
    ans = []
    if max(p_num) < int(n[0]):
        if (min(p_num) != 0):
            ans.append(str(p_num[0]))
        else:
            ans.append(str(p_num[1]))

        ans.append(str(min(p_num))*len(n))
        ans = int(''.join(ans))
        return ans

    flag = False
    for i, s in enumerate(n):
        for p in p_num:
            if len(ans) != 0 and int(s) < p:
                flag = True
                ans.append(str(p))
                ans.append(len(n[i:])*str(min(p_num)))
                break
            if int(s) <= p:
                ans.append(str(p))
                break

        if flag:
            break

    return int("".join(ans))


if __name__ == '__main__':
    ans = main()
    print(ans)
