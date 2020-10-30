def solution(a, b):
    answer = 0
    
    if a == b:
        return a
    elif a > b:
        return int(a * (a + 1) / 2 - (b - 1) * b / 2)
    else:
        return int(b * (b + 1) / 2 - (a - 1) * a / 2)