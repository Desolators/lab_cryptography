from random import randint
from math import gcd

e = 2448269
n = 3064049
k = 3
d = 2
x = 25
y = pow(x, e, n)
k1 = 2
d1 = 2
d_end = 2
while pow(y, d_end, n) != 25:
    while gcd(k, d) != 1 or abs((e / n) - (k / d)) >= (1 / (2 * (d * d))):
        k = randint(k1 + 1, 1000)
        d = randint(d1 + 1, 1000)
    print(k)
    print(d)
    k1 = k
    d1 = d
    d_end = d
    k = 2
    d = 2


# d, k = 5449, 3178
# while (e * d) - 1 != k * n:
#     d = randint(2, 10000)
#     k = randint( 2, 10000)
# print (d)

# def generator():
#     a, b = 2, 4
#     while gcd(a,b) != 1 or a > b:
#         a = randint(2, 10000)
#         b = randint(2, 10000)
#         print(a, b)
#
# # a1 = 1
# while a1:
#     generator()