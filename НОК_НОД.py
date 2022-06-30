def deli(a, b):
    return a if b == 0 else b if a % b == 0 else deli(b, a % b)


def nok(a, b):
    return a * b // deli(a, b)


print(deli(0, 5))
