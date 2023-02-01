import numpy as np
# -*- coding: utf-8 -*-
s = np.random.randint(0, 100, 100)
cumulative = [0]

for i in range(len(s)):
    cumulative.append(cumulative[i]+s[i])

for i in range(len(cumulative)):
    print(sum(s[0:i]), cumulative[i])

