def solution(n):
    answer = ''

    while n != 0:
        n, remainder = divmod(n, 3)
        if remainder == 0:
            answer = '4' + answer
            n -= 1
        elif remainder == 1:
            answer = '1' + answer
        else:
            answer = '2' + answer

    return answer