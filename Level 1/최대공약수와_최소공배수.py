def solution(n, m):
    gcf = 0
    lcm = 0
    
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcf = i
    
    lcm = (n * m) / gcf
    
    return [gcf, lcm]