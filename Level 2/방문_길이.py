def solution(dirs):
    position = (0, 0)   # x, y
    dxdy = {'U': (0, 1),
            'D': (0, -1),
            'L': (-1, 0),
            'R': (1, 0)}
    visited = set()
    
    for d in dirs:
        x, y = position
        dx, dy = dxdy[d]
        
        if -6 < x + dx < 6 and -6 < y + dy < 6:
            nx = x + dx
            ny = y + dy
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x = nx
            y = ny
    
        position = (x, y)
    
    
    return len(visited) // 2