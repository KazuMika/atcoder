r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

disr = r2-r1
disc = c2-c1
disr = abs(disr)
disc = abs(disc)

if disc == disr == 0:
    print(0)
elif disr == disc or (disr + disc) <= 3:
    print(1)
elif abs(disr-disc) % 2 == 0 or abs(disr-disc) <= 3:
    print(2)
elif abs(disr-disc) % 2 == 1 and abs(disr-disc) <= 3:
    print(2)
else:
    print(3)
