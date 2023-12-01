# import random
# n = 31459
# def find_x_y_z():
#     count = 0
#     d = 0
#     x, y, z = 1, 1, 1
#     y1, y2, y3 = 18707, 26871, 6384
#     y_0 = 11638
#     while d != y_0:
#         count += 1
#         x, y, z = random.randint(2, 1000), random.randint(2, 1000), random.randint(2, 1000)
#         a, b, c = pow(y1, x, n), pow(y2, y, n), pow(y3, z, n)
#         d = pow(a * b * c, 1, n)
#     print('x, y, z = ', x, y, z)
#     print('Попыток: ', count)
#     return x, y, z
# kek = find_x_y_z()
# x1, x2, x3 = 23, 755, 631
# a, b, c = pow(x1, kek[0], n), pow(x2, kek[1], n), pow(x3, kek[2], n)
# d = pow(a * b * c, 1, n)
# print('x = ', d)






import random


