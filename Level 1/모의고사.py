def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    points = {1:0, 2:0, 3:0}

    for problem in range(len(answers)):
        if answers[problem] == first[problem % len(first)]:
            points[1] += 1
        if answers[problem] == second[problem % len(second)]:
            points[2] += 1
        if answers[problem] == third[problem % len(third)]:
            points[3] += 1

    top = 0

    for point in points.keys():
        if top < points[point]:
            top = points[point]
            answer = [point]
        elif top == points[point]:
            answer.append(point)


    return answer