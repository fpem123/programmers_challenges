from itertools import permutations

def solution(numbers):
    answer = 0
    nums = set()
    numTable = []
    
    for i in range(1, len(numbers) + 1):
        nums.update(set(map(int, (map(''.join, permutations(numbers, i))))))
    
    m = max(nums)
    numTable = [False, False] + [True] * (m - 1)
    
    for i in range(2, m + 1):
        if numTable[i]:
            for j in range(i + i, m + 1, i):
                numTable[j] = False
    
    for num in nums:
        if numTable[num]:
            answer += 1
    
    return answer