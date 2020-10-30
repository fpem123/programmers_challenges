def solution(s):
    answer = ''
    i = 0
    
    for char in range(len(s)):
        if s[char] == ' ':
            answer += ' '
            i = 0
        else:
            if i % 2 == 0:
                answer += s[char].upper()
            else:
                answer += s[char].lower()
            i += 1
                 
    return answer