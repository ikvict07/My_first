
def largest_common_subsecuance(a,b):
    """Наибольшая общая подстрока"""
    mmax = 0
    p = 0
    F = [[0]*(len(b)+1) for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
                if F[i][j]>mmax:
                    mmax = F[i][j]
                    p = i


    return a[p-mmax:p]
a = [1,2,3,4,5,6,7,8,9,10,11,4,5,6,78]
b = ['a', 1, 2 ,3]
print(largest_common_subsecuance(b,a))
'''------------------------------------------'''
