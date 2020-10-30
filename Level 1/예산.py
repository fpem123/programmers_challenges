def solution(d, budget):
    answer = 0
    d.sort()
    
    for money in d:
        if money > budget:
            break
        budget -= money
        answer += 1
    
    return answer