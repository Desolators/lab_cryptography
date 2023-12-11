from sys import set_int_max_str_digits as mas_str
from sys import setrecursionlimit as mas_rec

mas_rec(2 ** 10)
mas_str(0)


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
