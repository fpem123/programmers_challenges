chars = "0123456789ABCDEF"

def change(num, notation):
    q, r = divmod(num, notation)
    
    if q == 0:
        return chars[r]
    else:
        return change(q, notation) + chars[r]


def solution(n, t, m, p):
    answer = ''
    game = ''
    num = 0
    
    while len(game) < t * m:
        game += change(num, n)
        num += 1
    
    for i in range(p - 1, len(game), m):
        answer += game[i]
    
    return answer[:t]