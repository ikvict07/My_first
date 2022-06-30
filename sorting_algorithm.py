'''сортировка слиянием'''


def merge(a: list, b: list) -> list:
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
        else:
            c[n] = b[k]
            k += 1
        n += 1
    c[n:] = a[i:] if i < len(a) else b[k:]
    return c


a = [1, 4, 8, 9, 12, 45]
b = [0, 6, 7, 74, 102, 1007]


def merge1(a: list, l: int) -> list:
    c = [0] * (len(a))
    i = n = 0
    li = l
    while i < l and li < len(a):
        if a[i] <= a[li]:
            c[n] = a[i]
            i += 1
        else:
            c[n] = a[li]
            li += 1
        n += 1
    c[n:] = a[li:] if li < len(a) else a[i:li]
    return c


c = [1, 4, 8, 9, 12, 45, 0, 6, 7, 74, 102, 1007]


def merge_sort(a: list):
    if len(a) <= 1:
        return
    middle = len(a) // 2
    L = a[:middle]
    R = a[middle:]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    a[:] = C[:]


l = [5, 748, 12, 465, 8, 42, 0, 57, 1, 8, 0, 2, 45, 74, 6374, 654, 78, 56, 18, 38, 1, 54, 7, 5, ]

'''Быстрая сортировка Тони Хоара'''


def quick_sort(a):
    if len(a) <= 1:
        return
    barrier = a[0]
    L = [i for i in a if i < barrier]
    M = [i for i in a if i == barrier]
    R = [i for i in a if i > barrier]
    quick_sort(L)
    quick_sort(R)

    k = 0
    for i in L + M + R:
        a[k] = i
        k += 1


# print(quick_sort(l))
print(l)

'''проверка на отсортированность O(n)'''


def is_sorted(a, ascending=True):
    for i in range(1, len(a)):
        if ascending:
            if a[i] < a[i - 1]:
                return False
        else:
            if a[i] > a[i - 1]:
                return False
    return True


print(is_sorted(l))
