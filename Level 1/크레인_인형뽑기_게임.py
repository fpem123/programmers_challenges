import numpy as np

def solution(board, moves):
    answer = 0
    stack = ['Im bottom']
    board = list(map(list, np.transpose(board)))
    
    print(board)
    
    for i in board:
        while 0 in i:
            i.remove(0)
            
    for i in moves:
        pose = i - 1
        if board[pose]:
            now = board[pose].pop(0)
            if now == stack[len(stack) - 1]:
                stack.pop()
                answer += 2
            else:
                stack.append(now)
                
    return answer