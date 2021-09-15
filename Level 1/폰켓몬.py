def solution(nums):
    answer = 0
    pick = len(nums) // 2
    kind = len(set(nums))
    
    print(pick, kind)
    
    return min(pick, kind)