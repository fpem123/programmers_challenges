import re

def InAndOut(day, end, t):
    h, m, s, ms = list(map(int, re.split('[:.]', end)))
    end = (h * 3600 + m * 60 + s) * 1000 + ms
    
    t = int(float(t[:-1]) * 1000) - 1
    start = end - t
            
    return start, end
    

def solution(lines):
    answer = 0
    newlines = []
    size = len(lines)
    
    for idx, line in enumerate(lines):
        day, end, t = line.split(" ")
        start, end = InAndOut(day, end, t)
        newlines.append((start, end))
    
    times = sorted(list(newlines), key=lambda x: x[0])
    
    for i, t1 in enumerate(times):
        cnt = 0
        
        for j, t2 in enumerate(times):
            if t1[1] <= t2[0] <= t1[1] + 999:
                cnt += 1
            elif t1[1] <= t2[1] <= t1[1] + 999:
                cnt += 1
            elif t2[0] <= t1[1] and t2[1] >= t1[1] + 999:
                cnt += 1
                
        answer = max(answer, cnt)
        
    return answer