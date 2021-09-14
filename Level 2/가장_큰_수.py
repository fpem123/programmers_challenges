from functools import cmp_to_key as cmp

def cm(x, y):
    a = x + y
    b = y + x
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    # 0~999
    numbers.sort(key = cmp(cm), reverse = True)
    #numbers.sort(key = lambda x: x*3, reverse = True)
    
    answer = str(int("".join(numbers)))

    return answer