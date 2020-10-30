def solution(s):
    answer = ''
    
    half, remainder = divmod(len(s), 2)
    
    if remainder == 0:
        answer = s[half - 1] + s[half]
    else:
        answer = s[half]
    
    return answer