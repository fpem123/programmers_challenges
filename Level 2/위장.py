from collections import Counter

def solution(clothes):
    answer = 1
    
    clothe = Counter([kind for name, kind in clothes])
    
    for i in clothe.values():
        answer *= (i + 1)
    
    return answer - 1