# Method 1 - Iterative

def calculate(x, n):
    res = 0
    for i in range(1, n+1):
        res += 1/(x**i)
    return res

# Method 2 - Recursive


def calculate(x, n):
    if n < 1:
        return 0
    return calculate(x, n-1) + (1/(x**n))


# print(calculate(4, 5))
