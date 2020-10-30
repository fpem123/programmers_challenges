def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    
    if not answer:
        return [-1]

    answer.sort()
    
    return answer