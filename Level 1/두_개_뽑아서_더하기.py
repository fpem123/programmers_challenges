def solution(numbers):
    answer = set()
    size = len(numbers)
    
    for one in range(size):
        for other in range(one + 1, size):
            answer.add(numbers[one]+ numbers[other])
    
    answer = list(answer)
    answer.sort()
    
    return answer