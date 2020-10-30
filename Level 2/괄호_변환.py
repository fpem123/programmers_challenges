def solution(p):
    answer = ''
    u = ''
    v = ''
    lb_count = 0
    rb_count = 0
    isCorrect = True
    
    for index in range(len(p)):
        u += p[index]
        
        if p[index] == '(':
            lb_count += 1
        else:
            rb_count += 1
        
        if lb_count == rb_count:
            v = p[index + 1:]
            break
            
    if v != '':
        v = solution(v)    
        
    for index in range(len(u)):
        if u[index] == '(':
            for j in range(index + 1, len(u)):
                if u[j] == ')':
                    break
            else:
                isCorrect = False
    
    if not isCorrect:
        answer = '(' + v + ')'
        u = u[1:-1]
        
        for bracket in u:
            if bracket == ')':
                answer += '('
            else:
                answer += ')'
    else:
        answer = u + v
    
    return answer