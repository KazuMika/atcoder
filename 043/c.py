def main():
    n = int(input())
    a = list(map(int, input().split()))
    n_min, n_max = min(a), max(a)
    ans = []

    if n_min == n_max:
        return 0

    for y in range(n_min, n_max+1):
        cost = 0
        for x in a:
            cost += (x-y)**2
        ans.append(cost)

    return min(ans)


if __name__ == '__main__':
    ans = main()
    print(ans)
