# nextNum(n) generates the first n values of the series
def nextNum(n):
    sign = True
    series = []
    for i in range(1, n+1):
        series.append((i*i) + (1 if sign else -1)*1)
        sign = not(sign)
    return series

# print(nextNum(8))