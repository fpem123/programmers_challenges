import numpy as np

def solution(key, lock):
    ksize = len(key)
    lsize = len(lock)
    nksize = ksize + lsize * 2 - 2
    nkey = [[0] * nksize for _ in range(nksize)]
    
    for i in range(ksize):
        for j in range(ksize):
            nkey[lsize - 1 + i][lsize - 1 + j] = key[i][j]
    
    for _ in range(4):
        for i in range(nksize - lsize + 1):
            for j in range(nksize - lsize + 1):
                flag = False
                
                for x in range(lsize):
                    for y in range(lsize):
                        if nkey[i + x][j + y] + lock[x][y] != 1:
                            flag = True
                            break
                    if flag:
                        break
                else:
                    return True
                
        lock = np.rot90(lock)
        
    else:
        return False