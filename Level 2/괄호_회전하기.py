def correctCheck(s):
    stack = []
    
    for c in s:
        if c in ("[", "(", "{"):
            stack.append(c)
        else:
            if not stack:
                return False
            if c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True

def solution(s):
    answer = 0
    s = list(s)
    size = len(s)
    
    if size % 2 == 1:
        return answer
    
    for step in range(size):
        s.append(s.pop(0))
        
        if correctCheck(s):
            answer += 1
    
    return answer