def solution(m, n, board):
    answer = 0
    dxdy = ((0, 1), (1, 0), (1, 1))
    board = [[board[j][i] for j in range(m - 1, -1, -1)] for i in range(n)]
    
    while True:
        popdict = {i: set() for i in range(n)}
        howmany = 0
        
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] == 0:
                    continue
                elif board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    popdict[i].update([j, j + 1])
                    popdict[i + 1].update([j, j + 1])

        for i in range(n):
            newline = []
            popitems = popdict[i]
            numOfPop = len(popitems)
            howmany += numOfPop

            for j in range(m):
                if j not in popitems:
                    newline.append(board[i][j])

            newline += [0] * numOfPop

            board[i] = newline
        
        
        if howmany == 0:
            break
        
        answer += howmany
    
    return answer