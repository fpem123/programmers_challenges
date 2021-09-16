def solution(n, results):
    answer = 0
    win = dict()
    matrix = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        win[i] = set()
    
    for result in results:
        win[result[0]-1].add(result[1]-1)
        
    while True:
        sig = True
        
        for winner in win:
            tmp = len(win[winner])
            losers = set()
            
            for loser in win[winner]:
                losers.update(win[loser])
            
            win[winner].update(losers)
        
            if not tmp == len(win[winner]):
                sig = False
        
        if sig:
            break

    for winner in win:
        for loser in win[winner]:
            matrix[winner][loser] = 1
            matrix[loser][winner] = -1
    
    for line in matrix:
        if line.count(0) == 1:
            answer += 1
    
    return answer