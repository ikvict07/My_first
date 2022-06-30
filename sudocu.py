import numpy as np
def valid_solution(board):
    npboard = np.array(board)
    for i in range(9):
        a=list(npboard[:,i])
        b=list(npboard[i,:])
        first = all([i in a for i in range(1,10)])
        secnd = all([i in b for i in range(1,10)])
        if not first or not secnd:
            return False
    for f in range(3,10,3):
        for s in range(3,10,3):
            c=[]
            for i in list(map(list,npboard[f-3:f,s-3:s])):
                for j in i:
                    c.append(j)
            kl = all([p in c for p in range(1,10)])
            if not kl:
                return False
    return True
