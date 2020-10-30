def solution(priorities, location):
    answer = 0
    q = []
    
    for i, priority in enumerate(priorities):
        q.append((i, priority))
    
    while q:
        item = q.pop(0)
        if not q:
            answer += 1
            break
        elif max(q, key=lambda x: x[1])[1] > item[1]:
            q.append(item)
        else:
            answer += 1
            if item[0] == location:
                break
    
    return answer