from sys import set_int_max_str_digits as mas_str
mas_str(0)


def fibonacci(n):
    if n <= 1:
        return n
    count, n = 0, 0
    n1, n2 = 0, 1
    while count != n - 1:
        n = n1 + n2
        n1, n2 = n2, n
        count += 1
    return n


def fibonacci_list(n):
    if n <= 1:
        return n
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[-1]
