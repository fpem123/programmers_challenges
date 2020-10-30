def solution(x, n):
    answer = []
    weight = x
    
    for i in range(n):
        answer.append(x)
        x = x + weight
    
    return answer