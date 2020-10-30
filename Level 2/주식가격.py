def solution(prices):
    answer = []
    queue = []
    
    for i, price in enumerate(prices):
        m = 0
        for j in range(i + 1, len(prices)):
            m += 1
            if price > prices[j]:
                break
                
        answer.append(m)
    
    return answer