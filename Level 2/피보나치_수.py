def solution(n):
    fib = [1, 1]
    
    for i in range(2, n):
        fib[i%2] = fib[(i - 1) % 2] + fib[(i - 2) % 2]
    
    return max(fib) % 1234567