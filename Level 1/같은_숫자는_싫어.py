def solution(arr):
    answer = ['im bottom']
    
    for num in arr:
        if answer[-1] != num:
            answer.append(num)
    
    answer.pop(0)
    
    return answer