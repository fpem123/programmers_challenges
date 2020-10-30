def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def solution(w,h):
    answer = 0
    g = gcd(w, h)
    
    answer = w * h - (w + h - g)
    
    return answer