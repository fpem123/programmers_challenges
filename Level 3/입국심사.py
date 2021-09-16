def solution(n, times):
    min_time = 1
    max_time = min(times) * n
    answer = 0
    
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        process_customer = 0
        
        for police in times:
            process_customer += mid_time // police
            
            if process_customer >= n:
                break
            
        if process_customer >= n:
            max_time = mid_time - 1
            answer = mid_time
        elif process_customer < n:
            min_time = mid_time + 1
    
    return answer