MINOR = 9999

def greedyTree(cur, index, notA, name, move):
    global MINOR
    right = cur
    left = cur
    r_len = 0
    l_len = 0
    
    while right != index:
        right = (right + 1) % len(name)
        r_len += 1
        
    while left != index:
        left = (left - 1) % len(name)
        l_len += 1
    
    move += min(r_len, l_len)
    
    if move > MINOR:
        return 0
    
    for i in notA:
        greedyTree(index, i, notA - {i}, name, move)
            
    if not notA:
        if move < MINOR:
            MINOR = move

def solution(name):
    name = list(name)
    answer = 0
    cur = 0
    notA = set()
    minor = len(name) + 1
    
    for index, word in enumerate(name):
        if ord(word) > ord('N'):
            answer += 13 - (ord(word) - 65) % 13
            notA.add(index)
        elif word == 'A':
            pass
        else:
            answer += (ord(word) - 65) % 14
            notA.add(index)
    
    for index in notA:
        greedyTree(cur, index, notA - {index}, name, 0)
    
    answer += MINOR
    
    return answer