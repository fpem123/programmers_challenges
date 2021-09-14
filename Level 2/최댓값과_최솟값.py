def solution(s):
    s = list(map(int, s.split(' ')))
    
    return '{} {}'.format(min(s), max(s))