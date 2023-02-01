# -*- coding: utf-8 -*-


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main():
    n = int(input())
    fct = factorization(n)
    ans = 0
    for f in fct:
        for i in range(1, f[1]+1):
            n = int(n/Def[0]**i))
            if n == 0:
                return ans
            else:
                ans += 1

    return ans


if __name__ == '__main__':
    ans=main()
    print(ans)
