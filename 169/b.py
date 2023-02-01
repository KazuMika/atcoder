# -*- coding: utf-8 -*-
def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        return 0

    border = 10**18
    ans = 0
    temp = 1
    for i in a:
        temp *= i
        if temp > border:
            ans = -1
            break
        else:
            ans = temp

    return ans


if __name__ == '__main__':
    ans = main()
    print(ans)
