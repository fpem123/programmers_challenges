def solution(board):
    answer = 0
    
    rows = len(board)
    columns = len(board[0])
    
    for x in range(rows):
        for y in range(columns):
            if x - 1 == -1 or y - 1 == -1:
                pass
            elif board[x][y] == 1:
                board[x][y] += min(board[x - 1][y], board [x][y - 1], board [x - 1][y - 1])
                
            if board[x][y] > answer:
                answer = board[x][y]
    
    return answer ** 2