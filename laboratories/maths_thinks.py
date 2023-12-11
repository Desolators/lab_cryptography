from math import ceil
from math import gcd
from math import sqrt
from random import randint
from sys import set_int_max_str_digits as mas_str
from sys import setrecursionlimit as mas_rec
mas_rec(2 ** 10)
mas_str(0)


def separate():
    print('---------------------------------------------------------------------------------------------------------')


def fibonacci(n):
    if n <= 1:
        return n
    count, n_result = 0, 0
    n1, n2 = 0, 1
    while count != n - 1:
        count += 1
        n_result = n1 + n2
        n1, n2 = n2, n_result
    return n_result


def fibonacci_list(n):
    if n <= 1:
        return n
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[-1]


def fibonacci_recursion_list(n, memory):
    if memory[n] != -1:
        return memory[n]
    if n <= 1:
        return n
    result = (fibonacci_recursion_list(n - 1, memory) + fibonacci_recursion_list(n - 2, memory))
    memory[n] = result
    return result


def check_prime(p, d=2):
    while d * d <= p and p % d:
        d += 1
    return d * d > p


def generate_simple_number_p_q(p, q):
    while not check_prime(p) or not check_prime(q):
        p = randint(100_000_000_000, 500_000_000_000)  # после 14 знаков начинает работать очень медленно
        q = randint(510_000_000_000, 999_999_999_999)
    return p, q


def gcd_full(a, b):
    x_0, x_1, y_0, y_1 = 1, 0, 0, 1
    if a < b:
        a, b = b, a
    for k in range(a):
        if a % b != 0:
            c = a // b
            a, b = b, a % b
            x_0, x_1, y_0, y_1 = x_1, (x_0 - c * x_1), y_1, (y_0 - c * y_1)
        else:
            return b, x_1, y_1


def open_key_search(fn):
    e = randint(2, randint(3, fn - fn // 4))
    while e != fn - 2:
        if gcd_full(fn, e)[0] == 1:
            return e
        else:
            e += 1


def alg_fact_ferma(N):
    assert N % 2 == 1
    a_square = ceil(sqrt(N))
    while sqrt((a_square * a_square) - N) % 1 > 0:
        a_square += 1
    a = int(a_square + sqrt((a_square * a_square) - N))
    b = int(a_square - sqrt((a_square * a_square) - N))
    return a, b


def encryption(*args, x, key):
    if key == "task_1":
        e, N = args
        y = pow(x, e, N)
        print(f"X = {x}, {e = }, {N = }")
        print(f"Ответ: Y = {y} ")
        return y, e

    if key == "automate":
        p, q = args
        N = p * q
        fn = (p - 1) * (q - 1)
        e1, d1, e2, d2 = find_keys_automate(fn)
        y = pow(x, e1, N)
        print(f"{p = }, {q = }, {N = }, φ(N) = {fn}")
        print(f"{e1 = }, {e2 = }")
        print(f"{d1 = }, {d2 = }")
        print(f"X = {x}")
        print(f"Y = {y} ")
        return y, e1, d1, e2, N

    if key == "rand":
        p, q = args
        N = p * q
        e1, d1, e2 = find_keys_p_q_rand(p, q)
        y1, y2 = pow(x, e1, N), pow(x, e2, N)
        print(f"{p = }, {q = }, {N = }")
        print(f"d = {d1}")
        print(f"X = {x}")
        print(f"Y1 = {y1}, Y2 = {y2}")
        return y1, e1, d1, e2, y2, N


def find_keys_automate(fn):
    e1, e2 = open_key_search(fn), open_key_search(fn)
    d1, d2 = pow(e1, -1, fn), pow(e2, -1, fn)
    while e1 == d1 or e2 == d2:
        e1, e2 = open_key_search(fn), open_key_search(fn)
        d1, d2 = pow(e1, -1, fn), pow(e2, -1, fn)
    return e1, d1, e2, d2


def find_keys_p_q_rand(p, q):
    fn = (p - 1) * (q - 1)
    e1, e2 = (open_key_search(fn)), (open_key_search(fn))
    d1, d2 = pow(e1, -1, fn), pow(e2, -1, fn)
    while e1 == d1 or e2 == d2:
        e1, e2 = open_key_search(fn), open_key_search(fn)
        d1, d2 = pow(e1, -1, fn), pow(e2, -1, fn)
    print(f"φ(N) = {fn}")
    print(f"{e1 = }, {e2 = }")
    print(f"{d1 = }, {d2 = }")
    return e1, d1, e2


def find_keys_ferma(e, N):
    p, q = alg_fact_ferma(N)
    fn = (p - 1) * (q - 1)
    d = pow(e, -1, fn)
    print(f"p = {p}, q = {q}, {N = }, φ(N) = {fn}")
    print(f"{e = }")
    print(f"Ответ: {d = }")
    return d


def decryption(y, d, N):
    x = pow(y, d, N)
    print(f"X = {x}")
    return x


def re_encryption(y, e, N, x0=2):
    while pow(x0, e, N) != y:
        x0 += 1
    print(f"Y = {y}, {e = }, {N = }")
    print(f"Методом перешифрования получаем исходный текст, Ответ x = {x0}")
    return x0


def re_encryption_or_krmd(y_0, e, N):
    y = y_0
    while y_0 != pow(y, e, N):
        y = (pow(y, e, N))
    print(f"Y = {y_0}, {e = }, {N = }")
    print(f"(методом перешифрования или бесключевое чтение с одним открытым ключом) Ответ: X = {y}")
    return y


def keyless_reading(y1, y2, e1, e2, N):
    _, r, s = gcd_full(e1, e2)
    if (e1 * r) + (e2 * s) != 1:
        r, s = s, r
    x = pow(y1, r, N) * pow(y2, s, N) % N
    print(f"Y1 = {y1}, Y2 = {y2}")
    print(f"{e1 = }, {e2 = }, {N = }")
    print(f"{r = }, {s = }")
    print(f"(методом бесключевого чтения) Ответ: X = {x}")
    return x


def generate_simple_number_p(p):
    while not check_prime(p):
        p = randint(25_000_000, 55_000_000)
    return p


def find_primitive_root(p):
    g = randint(2, generate_simple_number_p(4))
    fn = (p - 1)
    while pow(g, fn // 2, p) == 1:
        g += 1
    return g


def generate_p_x():
    p = generate_simple_number_p(4)
    x = randint(2, p - 2)
    return p, x


def create_y(g, x, p):
    y = pow(g, x, p)
    print(f"{y = }, {g = }, {p = }, {x = }")
    return y


def generate_k(k, p):
    while gcd(k, p - 1) != 1:
        k = randint(2, p - 3)
    return k


def hash_p_x_g_r_s_simple_generate(hash_, k, M=0):
    p, x, g, r, s = 0, 0, 0, 0, 0
    while gcd(k, p) != 1 or gcd(hash_, p) != 1 or not check_prime(p) or gcd(s, p - 1) != 1 or gcd(k, p - 1) != 1:
        p = generate_simple_number_p(4)
        if gcd(k, p - 1) == 1:
            x = randint(2, p - 3)
            g = find_primitive_root(p)
            r = pow(g, k, p)
            if M != 0:
                s = pow((M - x * r) * pow(k, -1, p - 1), 1, p - 1)
            else:
                s = (hash_ - x * r) * pow(k, -1, p - 1) % (p - 1)
    return p, x, g, r, s, M


def create_sign(p, x, g, k, hash_, text, key, M=0):
    separate()
    separate()
    y, r, s = 0, 0, 0
    # Задаем стартовые значения (формируем ключи)
    if g == 0 and key == 'no_secret':  # при этом условии включаем генератор и используем без секретного сообщения
        p, x = generate_p_x()
        g = find_primitive_root(p)
        y = create_y(g, x, p)
        k = generate_k(2, p)
        r = pow(g, k, p)
        s = (hash_ - x * r) * pow(k, -1, p - 1) % (p - 1)
    elif g != 0 and key == 'no_secret':  # при этом условии стартовые значения подаются из входа функции
        y = create_y(g, x, p)
        r = pow(g, k, p)
        s = (hash_ - x * r) * pow(k, -1, p - 1) % (p - 1)
    if g == 0 and key == 'secret':  # включаем генератор и используем в качестве K - секретное сообщение
        secrets = k
        generator = hash_p_x_g_r_s_simple_generate(hash_, secrets, M)
        p, x, g, r, s, M = generator
        y = create_y(g, x, p)
        print(f"Скрытое сообщние = {secrets}")
    elif g != 0 and key == 'secret':  # при этом условии берем значения из входа функции
        secrets = k
        y = create_y(g, x, p)
        r = pow(g, secrets, p)
        s = pow((M - x * r) * pow(secrets, -1, p - 1), 1, p - 1)
        print(f"Скрытое сообщние = {secrets}")
    print(f"Закрытый ключ (x) = {x}")
    print(f"Открытый ключ (p, g, y) = {p, g, y}")
    print(f"Хеш = {hash_}")
    separate()
    # Начинаем формирование цифровой подписи
    print(f"{k = }, {r = }, Обратный элемент k = {pow(k, -1, p - 1)}, {s = } ")
    if key == 'no_secret':
        digital_sign = text, r, s
        print("Цифровая подпись (Сообщение, r, s) = ", digital_sign)
        separate()
    elif key == 'secret':
        digital_sign = M, r, s
        print("Цифровая подпись (Сообщение, r, s) = ", digital_sign)
        separate()
    return y, r, p, s, x, g, key, hash_, M


def check_sign_and_secret_messg(hash_, hash_again, y, r, p, s, x, g, key, M=0):
    # Проверяем подлинность подписи
    ok = u'\u2713'  # значок галочки
    print("Проверка подписи: ")
    print(f"Проверка хеша = {hash_again} ")
    if hash_again == hash_:
        print(f"Получаем один и тот же хеш: {hash_again} = {hash_}")
        if key == 'no_secret':
            condition_1 = pow(y, r, p) * pow(r, s, p) % p
            condition_2 = pow(g, hash_again, p)
        else:
            condition_1 = pow(y, r, p) * pow(r, s, p) % p
            condition_2 = pow(g, M, p)
        if condition_1 == condition_2:
            print(f'Верная подпись {ok} {condition_1} = {condition_2}')
            if key == 'secret':
                secret_message = pow(s, -1, p - 1) * pow((M - x * r), 1, p - 1) % (p - 1)
                print(f"Получаем скрытое сообщение: {secret_message}")
                return secret_message
        else:
            print("Неверная цифровая подпись")
            print(f'{condition_1} != {condition_2}')
    else:
        print("Неверная цифровая подпись")
    pass


def first_algorithm_hash(message, p, alphabet):
    h_current = len(message)
    for i in range(len(message)):
        index_current = message[i]
        current_h = alphabet[index_current]
        h_current = pow(h_current + current_h, 2, p)
    return h_current


def second_alogrithm_hash(p, message):
    h_result = 0
    h_0 = len(str(message))
    h_current = str(message)
    for i in range(len(str(message))):
        h_now = h_current[i]
        h_result = pow(int(h_now) + 2 * h_0 + 1, 2, p - 1)
        h_0 = h_result
    return h_result + 1
