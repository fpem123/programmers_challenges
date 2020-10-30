def solution(n):
    root, remainder = divmod(n ** 0.5, 1)
    
    if remainder == 0:
        return int(root + 1) ** 2
    else:
        return -1