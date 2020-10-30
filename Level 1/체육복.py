result = []

def solution(n, lost, reserve):
    answer = 0
    count = n - len(lost)
    lost = set(lost)
    reserve = set(reserve)
    newlost = []
    
    for i in lost:
        if i in reserve:
            reserve -= {i}
            count += 1
        else:
            newlost.append(i)

    for i in newlost:
        if i - 1 in reserve:
            reserve -= {i - 1}
            count += 1
        elif i + 1 in reserve:
            reserve -= {i + 1}
            count += 1
    
            
    answer = count
    
    return answer