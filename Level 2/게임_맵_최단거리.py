def bfs(maps):
    dxdys = ((0, -1), (-1, 0), (0, 1), (1, 0))
    mapX = len(maps)
    mapY = len(maps[0])
    starting = (0, 0, 1)
    distances = [[999999999 for __ in range(mapY)] for _ in range(mapX)]
    queue = [starting]
    
    while queue:
        x, y, dst = queue.pop(0)
        distances[x][y] = dst
        
        for dx, dy in dxdys:
            nx = x + dx
            ny = y + dy
            ndst = dst + 1
            
            if 0 <= nx < mapX and 0 <= ny < mapY and ndst < distances[nx][ny]:

                if maps[nx][ny] == 1:
                    distances[nx][ny] = ndst
                    queue.append((nx, ny, ndst))
    
    return distances[-1][-1]

def solution(maps):
    answer = bfs(maps)
    
    if answer == 999999999:
        return -1
    
    return answer