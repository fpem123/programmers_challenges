def solution(n, edges):
    answer = 0
    visited = [False] * n
    visited[0] = True
    graph = dict()
    
    for edge in edges:
        graph.setdefault(edge[0] - 1, set()).add(edge[1] - 1)
        graph.setdefault(edge[1] - 1, set()).add(edge[0] - 1)
    
    curs = [0]
    
    while False in visited:
        nexts = []
        
        while curs:
            cur = curs.pop()
            
            for node in graph[cur]:
                if not visited[node]:
                    visited[node] = True
                    nexts.append(node)

        curs = nexts
                    
    return len(curs)