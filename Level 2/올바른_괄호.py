def solution(s):
    answer = True
    num = 0
    
    for i in s:
        if i == '(':
            num += 1
        elif num > 0:
            num -= 1
        else:
            return False

    return num == 0