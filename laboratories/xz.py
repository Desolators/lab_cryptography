from random import randint
from math import gcd

e = 2693216516134636609
n = 4617790059809965777
k = 3
d = 2
x = 25
y = pow(25, e, n)
k1 = 1
d1 = 1
d_end = 1
while pow(y, d_end, n) != 25:
    while gcd(k, d) != 1 or abs((e / n) - (k / d)) >= (1 / (2 * (d * d))):
        k = randint(k1 + 1, 10000)
        d = randint(d1 + 1, 10000)
    print(k)
    print(d)
    k1 = k
    d1 = d
    d_end = d
    k = 2
    d = 2
