def solution(n):
    size = 0
    for i in range(n + 1):
        size += i
    answer = [0] * size 
    num = 0
    cur = 0
    it = 0
    N = n
    
    while num != size:
        for i in range(0 + 2 * it, 0 + 2 * it + n):
            cur += i
            num += 1
            answer[cur] = num

        n -= 1

        for i in range(n):
            cur += 1
            num += 1
            answer[cur] = num

        n -= 1

        for i in range(n):
            cur -= (N - i)
            num += 1
            answer[cur] = num

        n -= 1
        N -= 1
        it += 1
    
    return answer