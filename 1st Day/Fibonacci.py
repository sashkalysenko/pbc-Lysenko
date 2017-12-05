def fibonacci(fib):
    """returns array of Fibonacci"""

    if fib < 0:
        return "input should be a positive number"
    elif fib == 1:
        return [0, 1]
    else:
        a = 0
        b = 1
        result = [0]
        for i in range(0, fib):
            c = a + b
            result.append(b)
            a = b
            b = c
        return result
