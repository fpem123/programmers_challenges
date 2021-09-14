def solution(n,a,b):
    answer = 1
    
    while not (abs(a - b) == 1 and (a + b) % 4 == 3):
        a = int(a / 2 + 0.5)
        b = int(b / 2 + 0.5)
        answer += 1
        
    return answer