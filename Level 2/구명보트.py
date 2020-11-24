def solution(people, limit):
    answer = 0
    size = len(people)
    oneCur = 0
    otherCur = size - 1
    people.sort(reverse=True)
    
    while otherCur - oneCur >= 1:
        if people[oneCur] + people[otherCur] <= limit:
            oneCur += 1
            otherCur -= 1
        else:
            oneCur += 1
            
        answer += 1
    if otherCur == oneCur:
        answer += 1
    
    return answer