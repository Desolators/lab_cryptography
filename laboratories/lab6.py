import maths_thinks as crypto

if __name__ == "__main__":
    crypto.separate()
    dict_alp = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12,
                'л': 13, 'м': 14, 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20, 'у': 21, 'ф': 22, 'х': 23,
                'ц': 24, 'ч': 25, 'ш': 26, 'щ': 27, 'ь': 28, 'ы': 29, 'ъ': 30, 'э': 31, 'ю': 32, 'я': 33}
    print("Сначала просто сделаем электронную подпись: ")
    text_1 = "овал"
    print(f'Наш текст, для которого применяем электронную подпись( Задание 1): {text_1}')
    hash__ = crypto.first_algorithm_hash(text_1, 79, dict_alp)
    y0, r0, p0, s0, x0, g0, k0, hash__1, M_1 = crypto.create_sign(p=79, x=2, g=15, k=7, hash_=hash__, text=text_1,
                                                                  key='no_secret')
    print('Теперь проверим подпись( Задание 2)')
    crypto.check_sign_and_secret_messg(hash_=hash__1, hash_again=hash__1, y=y0, r=r0, p=p0, s=s0, x=28, g=g0, key=k0)
    crypto.separate()
    print("Теперь проверим готовую электронную подпись( Задание 3): ")
    hash_task_3 = crypto.second_alogrithm_hash(59, 2205)
    crypto.check_sign_and_secret_messg(hash_=hash_task_3, hash_again=hash_task_3, y=27, r=13, p=59, s=29, x=8, g=14,
                                       key='no_secret', M=2205)
    crypto.separate()
    print("Теперь делаем передачу закрытого сообщения используя подпись( Задание 4): ")
    hash_2 = crypto.second_alogrithm_hash(2149163449, 1989582461)
    g_4 = crypto.find_primitive_root(3074929199)
    y1, r1, p1, s1, x1, g1, k1, hash__2, M_2 = crypto.create_sign(p=3074929199, x=28, g=5, k=2149163449, hash_=hash_2,
                                                                  text=1989582461, key='secret', M=1989582461)
    print('Теперь проверим подпись (и найдем секретное сообщение)')
    crypto.check_sign_and_secret_messg(hash_=hash__2, hash_again=hash__2, y=y1, r=r1, p=p1, s=s1, x=x1, g=g1,
                                       key='secret', M=M_2)
    crypto.separate()
    exit()
