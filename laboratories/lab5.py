from random import randint


def separator():
    return print("----------------------------------------------------")


def is_prime(p):
    d = 2
    while d * d <= p and p % d != 0:
        d += 1
    return d * d > p


def simple_number_p_q(p, q):
    while not is_prime(p) or not is_prime(q):
        p = randint(100000000000, 500000000000)  # после 14 знаков начинает работать очень медленно
        q = randint(510000000000, 999999999999)
    return p, q


def gcd(a, b):
    x_0, y_0 = 1, 0
    x_1, y_1 = 0, 1
    if a < b:
        a, b = b, a
    for k in range(a):
        if a % b != 0:
            c = a // b
            a, b = b, a % b
            x_0, x_1 = x_1, x_0 - c * x_1
            y_0, y_1 = y_1, y_0 - c * y_1
        else:
            return b, x_1, y_1


def open_key_search(fn, e):
    while e != fn - 2:
        if gcd(fn, e)[0] == 1:
            return e
        else:
            e += 1


def alg_fact_ferma(N):
    if N % 2 == 0:
        return "Error, even number"
    else:
        square_numb = 0
        k = 0
        while square_numb < N:
            k += 1
            square_numb = pow(k, 2)

        search_numb = pow((square_numb - N), 0.5)

        while search_numb % 1 > 0:
            k += 1
            square_numb = pow(k, 2)
            search_numb = pow((square_numb - N), 0.5)

        sqrt = pow(square_numb, 0.5)
        a = int(sqrt - search_numb)
        b = int(sqrt + search_numb)
        return a, b


def encryption(x, *args, key):
    if key == "task_1":
        e, N = args
        print(f"X = {x}, {e = }, {N = }")
        y = pow(x, e, N)
        print(f"Y = {y} ")
        return y, e

    if key == "automate":
        p, q = args
        N = p * q
        fn = (p - 1) * (q - 1)
        print(f"{p = }, {q = }, {N = }, φ(N) = {fn}")
        e_d = keys_automate(fn)
        y = pow(x, e_d[0], N)
        print(f"X = {x}")
        print(f"Y = {y} ")
        return y, e_d[0], e_d[1], e_d[2], N

    if key == "rand":
        p, q = args
        N = p * q
        print(f"{p = }, {q = }, {N = }")
        e_d = keys_p_q_rand(p, q)
        print(f"d = {e_d[1]}")
        print(f"X = {x}")
        y1, y2 = pow(x, e_d[0], N), pow(x, e_d[2], N)
        print(f"Y1 = {y1}, Y2 = {y2}")
        return y1, e_d[0], e_d[1], e_d[2], y2, N


def keys_automate(fn):
    e1, e2 = open_key_search(fn, randint(2, fn // 2)), open_key_search(fn, randint(2, fn // 2))
    d1, d2 = pow(e1, -1, fn), pow(e2, -1, fn)
    while e1 == d1 or e2 == d2:
        e1, e2 = open_key_search(fn, randint(2, fn // 2)), open_key_search(fn, randint(2, fn // 2))
        d1, d2 = pow(e1, -1, fn), pow(e2, -1, fn)
    print(f"{e1 = }, {e2 = }")
    print(f"{d1 = }, {d2 = }")
    return e1, d1, e2


def keys_p_q_rand(p, q):
    fn = (p - 1) * (q - 1)
    print(f"φ(N) = {fn}")
    e1, e2 = (open_key_search(fn, randint(2, fn // 2))), (open_key_search(fn, randint(2, fn // 2)))
    d1, d2 = pow(e1, -1, fn), pow(e2, -1, fn)
    while e1 == d1 or e2 == d2:
        e1, e2 = (open_key_search(fn, randint(2, fn // 2))), (open_key_search(fn, randint(2, fn // 2)))
        d1, d2 = pow(e1, -1, fn), pow(e2, -1, fn)
    print(f"{e1 = }, {e2 = }")
    print(f"{d1 = }, {d2 = }")
    return e1, d1, e2


def keys_ferma(e, N):
    p_q = alg_fact_ferma(N)
    fn = (p_q[0] - 1) * (p_q[1] - 1)
    print(f"p = {p_q[0]}, q = {p_q[1]}, {N = }, φ(N) = {fn}")
    print(f"{e = }")
    d = pow(e, -1, fn)
    print(f"{d = }")
    return d


def decryption(y, d, N):
    x = pow(y, d, N)
    print(f"X = {x}")
    return x


def re_encryption(y, e, N):
    x0 = 2
    print(f"Y = {y}, {e = }, {N = }")
    while pow(x0, e, N) != y:
        x0 += 1
    print(f"Методом перешифрования получаем исходный текст x: {x0}")
    return x0


def re_encryption_or_krmd(y_0, e, N):
    print(f"Y = {y_0}, {e = }, {N = }")
    y = y_0
    while y_0 != pow(y, e, N):
        y = (pow(y, e, N))
    print(f"X (методом перешифрования или бесключевое чтение с одним открытым ключом) = {y}")
    return y


def keyless_reading(y1, y2, e1, e2, N):
    print(f"Y1 = {y1}, Y2 = {y2}")
    print(f"{e1 = }, {e2 = }, {N = }")
    _, r, s = gcd(e1, e2)
    if (e1 * r) + (e2 * s) != 1:
        r, s = s, r
    print(f"{r = }, {s = }")
    x = pow(y1, r, N) * pow(y2, s, N) % N
    print(f"(методом бесключевого чтения) X = {x}")
    return x


if __name__ == '__main__':
    separator()
    separator()
    print("НАЧАЛО ЛАБОРАТОРНОЙ РАБОТЫ: ")
    separator()
    print("Задание 1, находим шифротекст Y имея исходный текст X, открытый ключ e, и модуль шифрования N: ")
    encryption(132, 17, 1739, key="task_1")  # x, e, N
    separator()
    separator()
    print("Задание 2, находим значение исходного текста X, имея модуль шифрования N, открытый ключ е, и  Y : ")
    re_encryption_or_krmd(66, 283, 377)  # y, e, N
    separator()
    re_encryption(66, 283, 377)  # y, e, N
    separator()
    separator()
    print("Задание 3, находим значение  d, имея  N, открытый ключ е (метод факторизации ферма): ")
    closed_key = keys_ferma(519, 4183)  # e, N
    separator()
    print("Задание 4, находим значение  X, имея  N, открытый ключ е и шифротекст Y : ")
    print("Метод перешифрования: ", )
    re_encryption_or_krmd(13, 7, 143)  # y, e, N
    separator()
    re_encryption(13, 7, 143)  # y, e, N
    separator()
    separator()
    print("Задание 5, найти методом бесключевого чтения исходный текст X, имея е1, е2, N и шифротексты Y1,Y2: ")
    keyless_reading(1682, 42, 7, 3, 3403)  # y1, y2, e, N
    re_encryption(42, 3, 3403)  # y, e, N
    separator()
    separator()
    print("НАЧАЛО ТЕСТОВ:")
    separator()
    separator()
    test = encryption(543, 1874947153801, 2797477623911, key="automate")  # x, p, q
    y_auto, e1_auto, d1_auto, e2_auto, N_auto = test
    decryption(y_auto, d1_auto, N_auto)  # y, d, N
    separator()
    re_encryption(y_auto, e1_auto, N_auto)  # y, e, N
    print("Дешифруем, и делаем вывод, что при перешифровании(x += 1) сложность дешифровки зависит от длины X")
    separator()
    print("Задаем псевдогенератором случайные простые p и q, и автоматически генерируем ключ e:")
    p_and_q = simple_number_p_q(20, 20)  # p, q
    plain_text = 42344411  # x
    rand_cypher_e_d = encryption(plain_text, p_and_q[0], p_and_q[1], key="rand")  # x, p, q
    y1_test, e1_test, d1_test, e2_test, y2_test, N_test = rand_cypher_e_d
    decryption(y1_test, d1_test, N_test)
    separator()
    separator()
    keyless_reading(y1_test, y2_test, e1_test, e2_test, N_test)
    separator()
    exit()
