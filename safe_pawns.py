import numpy as np


def safe_pawns(pawns: set):
    bar_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    bar_num = ['1', '2', '3', '4', '5', '6', '7', '8'][::-1]
    count = 0
    a = np.array([[0] * 8] * 8)
    for i in pawns:
        a[bar_num.index(i[1])][bar_l.index(i[0])] = 1
    for i, k in enumerate(a):
        for j, l in enumerate(k):
            if l == 1:
                try:
                    if a[i + 1][j - 1] == 1 or a[i + 1][j + 1] == 1:
                        count += 1
                except:
                    continue
    return count

# print(np.array([[0]*8]*8))
