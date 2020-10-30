def solution(n):
    answer = 0
    nums = [True] * (n + 1)

    nums[0] = False
    nums[1] = False

    for num in range(len(nums)):
        if nums[num]:
            for x in range(num + num, len(nums), num):
                nums[x] = False

    answer = nums.count(True)

    return answer