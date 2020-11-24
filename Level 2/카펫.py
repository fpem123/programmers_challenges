def solution(brown, yellow):
    answer = []
    area = brown + yellow
    
    for i in range(int(brown / 2)):
        for j in range(int(brown / 2)):
            if (3 + i) * (3 + j) == area and (1 + i) * (1 + j) == yellow:
                answer = [3 + i, 3 + j]
                break
    
    
    
    return sorted(answer, reverse=True)