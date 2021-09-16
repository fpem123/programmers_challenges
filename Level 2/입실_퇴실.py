def solution(enter, leave):
    size = len(enter)
    answer = [0] * size
    meet = {i + 1 : set() for i in range(size)}
    cur = 0
    room = set()
    
    while cur < size:
        if leave[cur] in room:
            for p in room:
                meet[p].update(room - {p})
            
            room.remove(leave[cur])
            cur += 1
        elif enter:
            room.add(enter.pop(0))
    
    for p, m in meet.items():
        answer[p - 1] = len(m)
    
    return answer