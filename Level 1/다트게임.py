def solution(dartResult):
    answer = 0
    dartResult = list(dartResult)
    starter = int(dartResult.pop(0))
    result = []
    stack = [starter]

    for char in dartResult:
        if char.isnumeric():
            if len(stack) == 1:
                stack[0] = 10
            else:
                result.append(stack)
                stack = [int(char)]
        else:
            stack.append(char)
    result.append(stack)

    Bonus = {'S':1, 'D':2, 'T':3}
    now_point = 0
    pre_point = 0

    for game in result:
        pre_point = now_point
        if len(game) == 2:
            now_point = game[0] ** Bonus[game[1]]
        else:
            now_point = game[0] ** Bonus[game[1]]
            if game[2] == '*':
                now_point *= 2
                pre_point *= 2
            else:
                now_point = -now_point
        answer += pre_point

    answer += now_point

    return answer