def dif(a, b):
    cnt = 0
    
    for i in range(len(a)):
        if not a[i] == b[i]:
            cnt +=1
            if cnt > 1:
                return False
    if cnt == 1:
        return True
    

def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    my_queue = [begin]
    
    if target not in words:
        return 0
    
    while False in visited:
        now = my_queue.pop()
        next_level = []
        false_count = visited.count(False)
        
        for i, word in enumerate(words):
            if dif(now, word) and not visited[i]:
                visited[i] = True
                next_level.append(word)
        
        my_queue = next_level
        answer += 1
        
        if target in my_queue:
            break
        
        if false_count == visited.count(False):
            break
    
    return answer