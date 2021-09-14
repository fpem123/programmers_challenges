def gcd(a, b):
    if b > a:
        a, b = b, a
    
    while b != 0:
        a, b = b, a % b
    
    return a


def lcm(a, b):
    return (a * b) / gcd(a, b)


def solution(arr):
    """
    answer = 0
    
    while len(arr) != 1:
        num1 = arr.pop(0)
        num2 = arr.pop(0)
        
        arr.append(lcm(num1, num2))
        
    return arr[0]
    """
    answer = arr.pop(0)
    
    for num in arr:
        answer = lcm(answer, num)    
    
    return answer