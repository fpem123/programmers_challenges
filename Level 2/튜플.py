def solution(s):
    answer = []
    new = set()
    s = s[2:-2].split('},{')
    s.sort(key=lambda x:len(x))
    
    for i in s:
        i = set(map(int, i.split(',')))
        num = i - new
        new.update(num)
        answer.append(num.pop())
    
    return answer