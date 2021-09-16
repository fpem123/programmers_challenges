def solution(msg):
    answer = []
    chardict = {chr(i+64): i for i in range(1, 27)}
    size = len(msg)
    visited = [False] * size
    
    for i in range(size):
        if visited[i]:
            continue
        char = ""
        
        for j in range(i, size):
            nchar = char + msg[j]
            
            if nchar not in chardict:
                chardict[nchar] = len(chardict) + 1
                break
                
            char = nchar
            visited[j] = True
            
        answer.append(chardict[char])
    
    return answer