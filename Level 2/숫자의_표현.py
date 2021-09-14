def solution(n):
    answer = 0
    cur = n
    
    while cur != 0:
        tmp = 0

        for num in range(cur, 0, -1):
            tmp += num
            
            if tmp == n:
                answer += 1
                break
            elif tmp > n:
                break
        
        cur -= 1
            
    
    return answer