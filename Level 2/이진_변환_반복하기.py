def solution(s):
    answer = [0, 0]
    
    while len(s) != 1:
        answer[0] += 1
        answer[1] += s.count('0')
        s = bin(s.count('1'))[2:]
    
    return answer