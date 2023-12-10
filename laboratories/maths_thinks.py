def fibonacci(n):
    if n <= 1:
        return n
    count, result = 0, 0
    n1, n2 = 0, 1
    while count != n - 1:
        result = n1 + n2
        n1, n2 = n2, result
        count += 1
    return result


print(fibonacci(10))
