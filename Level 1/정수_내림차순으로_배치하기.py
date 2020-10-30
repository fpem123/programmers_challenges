def solution(n):
    n = sorted(list(str(n)), reverse = True)
    n = "".join(n)
    return int(n)