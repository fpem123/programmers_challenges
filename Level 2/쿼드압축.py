def solution(arrs):
    answer = []
    one = 0
    zero = 0
    
    def separate(arr):
        zo = [0, 0]
        length = len(arr)
        summation = 0
        
        for i in arr:
            summation += sum(i)
        
        if summation == length * length:
            return [0, 1]
        elif summation == 0:
            return [1, 0]
        
        size = len(arr) // 2
        
        for i in range(0, length, size):
            for j in range(0, length, size):
                tmp = []
                for x in range(size):
                    a = []
                    for y in range(size):
                        a.append(arr[i+x][j+y])
                    tmp.append(a)
                result = separate(tmp)
                zo[0] += result[0]
                zo[1] += result[1]
        
        return zo
                
                
    answer = separate(arrs)
    
    
    return answer