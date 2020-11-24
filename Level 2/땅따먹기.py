def solution(land):

    land.append([0,0,0,0])
    
    for line in range(1, len(land)):
        for i in range(4):
            land[line][i] += max(land[line-1][:i] + land[line-1][i+1:])

    return max(land[-1])