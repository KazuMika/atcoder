s = "paper"
t = "title"
d1, d2 = {}, {}

for i, val in enumerate(s):
    d1[val] = d1.get(val, []) + [i]
for i, val in enumerate(t):
    d2[val] = d2.get(val, []) + [i]
print(d1, d2)

print(sorted(d1.values()))
print(sorted(d2.values()))
