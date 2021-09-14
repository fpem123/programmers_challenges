def solution(s):
    my_stack = [0]
    
    for word in s:
        if word == my_stack[-1]:
            my_stack.pop()
        else:
            my_stack.append(word)
            
    if len(my_stack) == 1:
        return 1
    
    return 0