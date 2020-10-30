def DFS(number, numbers, target, index):

    if index == len(numbers):
        if number == target:
            return 1
        else:
            return 0
    
    now = numbers[index]
    way = 0
    
    way += DFS(number + now, numbers, target, index + 1)
    way += DFS(number - now, numbers, target, index + 1)
    
    return way
    

def solution(numbers, target):
    answer = 0
    
    number = numbers[0]
    
    answer += DFS(number, numbers, target, 1)
    answer += DFS(-number, numbers, target, 1)
    
    return answer