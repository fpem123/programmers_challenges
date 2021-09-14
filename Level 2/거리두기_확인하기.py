def pFinder(place):
    coors = []
    
    for i, line in enumerate(place):
        for j, char in enumerate(line):
            if char == 'P':
                coors.append((i, j, 0))
    
    return coors
    
def bfs(place, coors):
    if not coors:
        return True
    
    nextCoors = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    while coors:
        queue = [coors.pop(0)]
        visited = [[False for _ in range(5)] for __ in range(5)]
        
        while queue:
            x, y, dst = queue.pop(0)
            visited[x][y] = True
            
            for dx, dy in nextCoors:
                nx = x + dx
                ny = y + dy
                ndst = dst + 1
                
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    visited[nx][ny] = True

                    if place[nx][ny] == 'P' and ndst <= 2:
                        return False
                    elif place[nx][ny] == 'O' and dst <= 1:
                        queue.append((nx, ny, ndst))
    
    return True

def solution(places):
    answer = []
    
    for place in places:
        coors = pFinder(place)
        
        if bfs(place, coors):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer