x, k, d = map(int, input().split())  # x現在地,k 移動回数,D移動できる距離
x = abs(x)
a = x // d  # 移動できる回数
b = x % d  # 移動した特のあまり
if k <= a:  # 移動する回数がkより大きいとき
    x = x - (k*d)
else:
    k = k - a  # ここで最短
    if k % 2 == 0:
        x = x - (a * d)
    else:
        x = x - (a * d)
        if x > 0:
            x = x - abs(d)
        else:
            x = x + abs(d)

print(abs(x))
