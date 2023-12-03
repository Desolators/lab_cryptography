from random import randint
from hashlib import sha512
from math import gcd


def separate():
    return print("----------------------------------------------------")


def prime_check(n, d=2):
    while d * d <= n and n % d:
        d += 1
    return d * d > n


def generate_simple_number_p(p):
    while not prime_check(p):
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


def hash_p_x_g_r_s_simple_generate(hash_, k):
    p, x, g, r, s = 0, 0, 0, 0, 0
    while gcd(k, p) != 1 or gcd(hash_, p) != 1 or not prime_check(p) or gcd(s, p - 1) != 1 or gcd(k, p - 1) != 1:
        p = generate_simple_number_p(4)
        if gcd(k, p - 1) == 1:
            x = randint(2, p - 3)
            g = find_primitive_root(p)
            r = pow(g, k, p)
            s = (hash_ - x * r) * pow(k, -1, p - 1) % (p - 1)
    return p, x, g, r, s


def create_sign(p, x, g, k, hash_, text, key):
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
        print(f"Скрытое сообщние = {secrets}")
        generator = hash_p_x_g_r_s_simple_generate(hash_, secrets)
        p, x, g, r, s = generator
        y = create_y(g, x, p)
    elif g != 0 and key == 'secret':  # при этом условии берем значения из входа функции
        secrets = k
        print(f"Скрытое сообщние = {secrets}")
        y = create_y(g, x, p)
        r = pow(g, secrets, p)
        s = (hash_ - x * r) * pow(secrets, -1, p - 1) % (p - 1)
    print(f"Закрытый ключ (x) = {x}")
    print(f"Открытый ключ (p, g, y) = {p, g, y}")
    print(f"Хеш = {hash_}")
    separate()
    # Начинаем формирование цифровой подписи
    print(f"{k = }, {r = }, Обратный элемент k = {pow(k, -1, p - 1)}, {s = } ")
    digital_sign = text, r, s
    print("Цифровая подпись (Сообщение, r, s) = ", digital_sign)
    separate()
    return y, r, p, s, x, g, key, hash_


def check_sign_and_secret_messg(hash_, hash_again, y, r, p, s, x, g, key):
    # Проверяем подлинность подписи
    ok = u'\u2713'  # значок галочки
    print("Проверка подписи: ")
    print(f"Проверка хеша = {hash_again} ")
    if hash_again == hash_:
        print(f"Получаем один и тот же хеш: {hash_again} = {hash_}")
        condition_1 = pow(y, r, p) * pow(r, s, p) % p
        condition_2 = pow(g, hash_again, p)
        if condition_1 == condition_2:
            print(f'Верная подпись {ok} {condition_1} = {condition_2}')
            if key == 'secret':
                secret_message = pow(s, -1, p - 1) * pow(hash_again - (x * r), 1, p - 1) % (p - 1)
                print(f"Получаем скрытое сообщение: {secret_message}")
                return secret_message
        else:
            print("Неверная цифровая подпись")
            exit()
    else:
        print("Неверная цифровая подпись")
        exit()
    pass


if __name__ == "__main__":
    separate()
    print("Сначала просто сделаем электронную подпись: ")
    text_1 = "Privet medved"
    print(f'Наш текст, для которого применяем электронную подпись: {text_1}')
    hash__ = int(sha512(text_1.encode("utf-8")).hexdigest(), 16) % 10 ** 5
    y0, r0, p0, s0, x0, g0, k0, hash__1 = create_sign(p=11, x=3, g=0, k=0, hash_=hash__, text=text_1, key='no_secret')
    print('Теперь проверим подпись')
    check_sign_and_secret_messg(hash_=hash__1, hash_again=hash__1, y=y0, r=r0, p=p0, s=s0, x=x0, g=g0, key=k0)
    separate()
    print("Теперь делаем передачу закрытого сообщения используя подпись: ")
    text_2 = "Privet"
    print(f'Наш текст, для которого применяем электронную подпись: {text_2}')
    hash_2 = int(sha512(text_2.encode("utf-8")).hexdigest(), 16) % 10 ** 5
    y1, r1, p1, s1, x1, g1, k1, hash__2 = create_sign(p=11, x=3, g=0, k=123, hash_= hash_2, text=text_2, key='secret')
    print('Теперь проверим подпись (и найдем секретное сообщение)')
    check_sign_and_secret_messg(hash_=hash__2, hash_again=hash__2, y=y1, r=r1, p=p1, s=s1, x=x1, g=g1, key=k1)
    separate()
    exit()
