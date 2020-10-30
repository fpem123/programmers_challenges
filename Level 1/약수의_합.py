def solution(n):
    answer = []
    
    for num in range(1, (n // 2) + 1):
        if n % num == 0:
            answer.append(num)
    
    return sum(answer) + n