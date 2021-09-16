def solution(m, n, puddles):
    answer = 0
    village = [[0 for j in range(m + 1)] for i in range(n + 1)]
    village[1][1] = 1
    
    for x in range(1, n+1):
        for y in range(1, m+1):
            if x == 1 and y == 1:
                continue
            
            if [y, x] in puddles:
                village[x][y] = 0
            else:
                village[x][y] = village[x - 1][y] + village[x][y - 1]
                village[x][y] %= 1000000007
                    
    return village[x][y]