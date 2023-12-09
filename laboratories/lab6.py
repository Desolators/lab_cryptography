from math import gcd
from random import randint


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


def hash_p_x_g_r_s_simple_generate(hash_, k, M=0):
    p, x, g, r, s = 0, 0, 0, 0, 0
    while gcd(k, p) != 1 or gcd(hash_, p) != 1 or not prime_check(p) or gcd(s, p - 1) != 1 or gcd(k, p - 1) != 1:
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
        print(f"Скрытое сообщние = {secrets}")
        generator = hash_p_x_g_r_s_simple_generate(hash_, secrets, M)
        p, x, g, r, s, M = generator
        y = create_y(g, x, p)
    elif g != 0 and key == 'secret':  # при этом условии берем значения из входа функции
        secrets = k
        print(f"Скрытое сообщние = {secrets}")
        y = create_y(g, x, p)
        r = pow(g, secrets, p)
        s = pow((M - x * r) * pow(secrets, -1, p - 1), 1, p - 1)
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


if __name__ == "__main__":
    separate()
    dict_alp = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12,
                'л': 13, 'м': 14, 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20, 'у': 21, 'ф': 22, 'х': 23,
                'ц': 24, 'ч': 25, 'ш': 26, 'щ': 27, 'ь': 28, 'ы': 29, 'ъ': 30, 'э': 31, 'ю': 32, 'я': 33}
    print("Сначала просто сделаем электронную подпись: ")
    text_1 = "овал"
    print(f'Наш текст, для которого применяем электронную подпись( Задание 1): {text_1}')
    hash__ = first_algorithm_hash(text_1, 79, dict_alp)
    y0, r0, p0, s0, x0, g0, k0, hash__1, M_1 = create_sign(p=79, x=2, g=15, k=7, hash_=hash__, text=text_1,
                                                           key='no_secret')
    print('Теперь проверим подпись( Задание 2)')
    check_sign_and_secret_messg(hash_=hash__1, hash_again=hash__1, y=y0, r=r0, p=p0, s=s0, x=28, g=g0, key=k0)
    separate()
    print("Теперь проверим готовую электронную подпись( Задание 3): ")
    hash_task_3 = second_alogrithm_hash(59, 2205)
    check_sign_and_secret_messg(hash_=hash_task_3, hash_again=hash_task_3, y=27, r=13, p=59, s=29, x=8, g=14,
                                key='no_secret', M=2205)
    print("Теперь делаем передачу закрытого сообщения используя подпись( Задание 4): ")
    hash_2 = second_alogrithm_hash(2149163449, 1989582461)
    g_4 = find_primitive_root(2149163449)
    y1, r1, p1, s1, x1, g1, k1, hash__2, M_2 = create_sign(p=2149163449, x=28, g=0, k=1535, hash_=hash_2,
                                                           text=1989582461, key='secret', M=1989582461)
    print('Теперь проверим подпись (и найдем секретное сообщение)')
    check_sign_and_secret_messg(hash_=hash__2, hash_again=hash__2, y=y1, r=r1, p=p1, s=s1, x=x1, g=g1, key='secret',
                                M=M_2)
    separate()
    exit()
