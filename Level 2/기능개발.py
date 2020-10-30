def solution(progresses, speeds):
    answer = []
    queue = []

    for index in range(len(progresses)):
        queue.append([progresses[index], speeds[index]])

    while queue:
        for job in queue:
            job[0] += job[1]

        done = 0

        while queue[0][0] >= 100:
            done += 1
            queue.pop(0)
            if not queue:
                break

        if done != 0:
            answer.append(done)

    return answer