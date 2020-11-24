def solution(n):
    ones = bin(n)[2:].count('1')
    
    while True:
        n += 1
        if bin(n)[2:].count('1') == ones:
            break
    
    return n