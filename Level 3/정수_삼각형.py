def solution(triangle):
    answer = 0
    triangle_size = len(triangle)
    
    for step in range(1, triangle_size):
        for i in range(len(triangle[step])):
            if i == 0:
                triangle[step][i] += triangle[step - 1][i]
            elif i == len(triangle[step]) - 1:
                triangle[step][i] += triangle[step - 1][i - 1]
            else:
                triangle[step][i] += max(triangle[step - 1][i], 
                                        triangle[step - 1][i - 1])
    
    answer = max(triangle[triangle_size - 1])
    
    return answer