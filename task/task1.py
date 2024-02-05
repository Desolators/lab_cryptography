N = 4
size = N + N
massive = [i for i in range(size)]
massive = [0, 0, 2, 2, 0, 2, 2, 0]
otvet = 0
for elem in massive:
    if elem > 0:
        otvet += (elem -1)
print(otvet)