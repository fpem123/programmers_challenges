def solution(participant, completion):
    answer = ''
    a = dict()
    b = dict()
    
    for i in participant:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    
    for i in completion:
        if i in a:
            a[i] -= 1
            if a[i] == 0:
                del a[i]
    
    a = list(a.keys())
    
    return a[0]