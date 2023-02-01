import numpy as np


def main():

    h, w, k = map(int, input().split())
    c = []
    blacks = []
    all_b = 0
    ans = 0

    for i in range(h):
        temp = input()
        temp_list = []
        for t in temp:
            temp_list.append(t)

        c.append(temp_list)
        blacks.append(c[i].count('#'))
        all_b += blacks[i]

    c_t = np.array(c).T.tolist()

    if all_b == k:
        ans += 1
        return ans

    for i in range(h):
        if k == all_b - blacks[i]:
            ans += 1

    for i in range(w):
        if k == all_b - c_t[i].count('#'):
            ans += 1

    for i in range(h):
        s = blacks[i]
        for j in range(i+1, h):
            if i != j:
                if k == all_b - s - blacks[j]:
                    ans += 1

    for i in range(w):
        temp = c_t[i].count('#')
        for j in range(i+1, w):
            if i != j:
                temp_2 = c_t[j].count('#')
                if k == all_b - temp - temp_2:
                    ans += 1

    for i in range(h):
        s = blacks[i]
        for j in range(w):
            counter_t = c_t[j].count('#')
            if k == all_b - counter_t - s:
                ans += 1

    return ans


if __name__ == '__main__':
    ans = main()
    print(ans)
