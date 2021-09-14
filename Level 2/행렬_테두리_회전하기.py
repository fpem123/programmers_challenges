def solution(rows, columns, queries):
    answer = []
    matrix  = []
    tmp = []
    
    for number in range(1, rows * columns + 1):
        tmp.append(number)
        
        if number % columns == 0:
            matrix.append(tmp)
            tmp = []
    
    for query in queries:
        x1 = query[0] - 1
        y1 = query[1] - 1
        x2 = query[2] - 1
        y2 = query[3] - 1
        tmp = matrix[x1][y1]
        smallNumber = tmp
        
        for x in range(x1, x2):
            value = matrix[x + 1][y1]
            matrix[x][y1] = value
            smallNumber = min(smallNumber, value)
        for y in range(y1, y2):
            value = matrix[x2][y + 1]
            matrix[x2][y] = value
            smallNumber = min(smallNumber, value)
        for x in range(x2, x1, -1):
            value = matrix[x - 1][y2]
            matrix[x][y2] = value
            smallNumber = min(smallNumber, value)
        for y in range(y2, y1, -1):
            value = matrix[x1][y - 1]
            matrix[x1][y] = value
            smallNumber = min(smallNumber, value)
        
        matrix[x1][y1 + 1] = tmp
        
        answer.append(smallNumber)
    
    return answer