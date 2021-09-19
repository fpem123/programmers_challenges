from queue import PriorityQueue

def solution(jobs):
    answer = 0
    q = PriorityQueue()
    size = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])
    jobs = sorted(jobs, key=lambda x: x[0])
    a, t = jobs.pop(0)
    q.put((t, a))
    time = a

    while not q.empty():
        t, a = q.get()
        time += t
        answer += time - a

        while jobs:
            if jobs[0][0] <= time:
                a, t = jobs.pop(0)
                q.put((t, a))
            else:
                break

        if q.empty() and jobs:
            a, t = jobs.pop(0)
            q.put((t, a))
            time = a

    return answer // size