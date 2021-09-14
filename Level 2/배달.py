from queue import PriorityQueue

def floyd(matrix, N):
    for via in range(N):
        for start in range(N):
            for dest in range(N):
                matrix[start][dest] = min(matrix[start][dest],
                                         matrix[start][via] + matrix[via][dest])
    
    return matrix

def dijkstra():
    pass

def solution(N, road, K):
    answer = 0
    matrix = [[float('inf') for i in range(N)] for j in range(N)]
    visited = [False for _ in range(N)]
    distance = [float('inf') for _ in range(N + 1)]
    distance[1] = 0
    q = PriorityQueue()
    
    for a, b, c in road:
        matrix[a - 1][b - 1] = min(c, matrix[a - 1][b - 1])
        matrix[b - 1][a - 1] = min(c, matrix[a - 1][b - 1])
        
    for i in range(N):
        matrix[i][i] = 0
    
    q.put([1, 0])
    
    while not q.empty():
        town, dst = q.get()
        
        if dst > distance[town]:
            continue
        
        for start, dest, ddst in road:
            ndst = dst + ddst
            
            if start == town and ndst < distance[dest]:
                distance[dest] = ndst
                q.put([dest, ndst])
            elif dest == town and ndst < distance[start]:
                distance[start] = ndst
                q.put([start, ndst])
    
    matrix = floyd(matrix, N)
    
    for dst in matrix[0]:
        if dst <= K:
            answer += 1
    
    return answer