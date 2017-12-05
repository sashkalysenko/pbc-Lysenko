def fibonacci(fib):
    a = 0
    b = 1
    result = [0]
    for i in range(0, fib - 1):
        c = a + b
        result.append(b)
        a = b
        b = c
    print(result)
