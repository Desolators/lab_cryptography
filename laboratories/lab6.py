from random import randint
from hashlib import sha512
from math import gcd


def separator():
    return print("----------------------------------------------------")


def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def simple_number_p(p):
    while not is_prime(p):
        p = randint(25000000, 55000000)
    return p


def primitive_root(p):
    g = randint(2, simple_number_p(4))
    fn = (p - 1)
    condition = int(fn / 2)
    while pow(g, condition, p) == 1:
        g += 1
    return g


def generate_p_x():
    p = simple_number_p(4)
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


def hash_p_x_simple_generator(hash_, secret):
    p, x, g, r, s = 0, 0, 0, 0, 0
    while gcd(secret, p) != 1 or gcd(hash_, p) != 1 or not is_prime(p) or gcd(s, p - 1) != 1 or gcd(secret, p - 1) != 1:
        p = simple_number_p(4)
        if gcd(secret, p - 1) == 1:
            x = randint(2, p - 3)
            g = primitive_root(p)
            r = pow(g, secret, p)
            s = (hash_ - x * r) * pow(secret, -1, p - 1) % (p - 1)
    return p, x, g, r, s


def sign(p, x, g, k, hash_, text, key):
    separator()
    separator()
    hash_again = hash_
    y, r, s = 0, 0, 0
    ok = u'\u2713'  # значок галочки
    # Задаем стартовые значения (формируем ключи)
    if g == 0 and key == 'no_secret':  # при этом условии включаем генератор и используем без секретного сообщения
        p, x = generate_p_x()
        g = primitive_root(p)
        y = create_y(g, x, p)
        k = generate_k(2, p)
        hash_again = int(sha512(text.encode("utf-8")).hexdigest(), 16) % 10 ** 5
        r = pow(g, k, p)
        s = (hash_ - x * r) * pow(k, -1, p - 1) % (p - 1)
    elif g != 0 and key == 'no_secret':  # при этом условии стартовые значения подаются из входа функции
        y = create_y(g, x, p)
        r = pow(g, k, p)
        s = (hash_ - x * r) * pow(k, -1, p - 1) % (p - 1)
    if g == 0 and key == 'secret':  # включаем генератор и используем в качестве K - секретное сообщение
        secrets = k
        print(f"Скрытое сообщние = {secrets}")
        generator = hash_p_x_simple_generator(hash_, secrets)
        p, x, g, r, s = generator
        y = create_y(g, x, p)
        hash_again = int(sha512(text.encode("utf-8")).hexdigest(), 16) % 10 ** 5
    elif g != 0 and key == 'secret':  # при этом условии берем значения из входа функции
        secrets = k
        print(f"Скрытое сообщние = {secrets}")
        y = create_y(g, x, p)
        r = pow(g, secrets, p)
        s = (hash_ - x * r) * pow(secrets, -1, p - 1) % (p - 1)
    print(f"Закрытый ключ (x) = {x}")
    open_key = p, g, y
    print(f"Открытый ключ (p, g, y) = {open_key} ")
    print(f"Хеш = {hash_}")
    separator()
    # Начинаем формирование цифровой подписи
    print(f"{k = }, {r = }, Обратный элемент k = {pow(k, -1, p - 1)}, {s = } ")
    signs = text, r, s
    print("Цифровая подпись (Сообщение, r, s) = ", signs)
    separator()
    # Проверяем подлинность подписи
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
        else:
            print("Неверная цифровая подпись")
            exit()
    else:
        print("Неверная цифровая подпись")
        exit()


if __name__ == "__main__":
    separator()
    print("Сначала просто сделаем электронную подпись: ")
    text_1 = "Privet medved"
    print(f'Наш текст, для которого применяем электронную подпись: {text_1}')
    hash_1 = int(sha512(text_1.encode("utf-8")).hexdigest(), 16) % 10 ** 5
    sign(11, 3, 0, 0, hash_1, text_1, key='no_secret')  # При g = 0, k = 0 включается генератор!
    separator()
    print("Теперь делаем передачу закрытого сообщения используя подпись: ")
    text_2 = "Privet"
    print(f'Наш текст, для которого применяем электронную подпись: {text_2}')
    hash_2 = int(sha512(text_2.encode("utf-8")).hexdigest(), 16) % 10 ** 5
    sign(11, 3, 0, 255, hash_2, text_2, key='secret')  # При g = 0 включается генератор!
    separator()
    exit()
