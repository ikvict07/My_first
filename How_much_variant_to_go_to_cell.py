import numpy as np

l, f = map(int, input().split())
z = tuple(map(int, input().split()))


def foo(n: int, m: int, k: tuple) -> int:
    """Сколько способов добраться в клетку k на поле n*m(если ходить только вправо и вниз)"""

    field = np.zeros((n + 1, m + 1), dtype=int)
    field[1, 1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            field[i][j] = field[i][j - 1] + field[i - 1][j]
    print(field[1:, 1:])
    return field[k[0], k[1]]


print(foo(l, f, z))
