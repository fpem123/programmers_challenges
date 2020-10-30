def solution(num):
    answer = 0
    
    for i in range(500):
        if num == 1:
            break
            
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
            
        answer += 1
    
    
    return answer if num == 1 else -1