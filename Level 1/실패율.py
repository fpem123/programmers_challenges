from collections import Counter

def solution(N, stages):
    answer = []
    user = Counter(stages)
    all_user = len(stages)
    
    for i in range(1, N + 1):
        if all_user == 0:
            answer.append([i, 0])
            continue
        weight = user[i] / all_user
        all_user -= user[i]
        answer.append([i, weight])
    
    answer.sort(key = lambda x: x[1], reverse = True)
    
    for i in range(N):
        answer[i] = answer[i][0]
    
    return answer