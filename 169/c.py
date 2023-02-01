from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
a, b = input().split()
a = int(a)
b = (Decimal(b) * Decimal(100))
ans = int(a*b)
print(int(Decimal(ans)/Decimal(100)))
