def solution(bridge_length, weight, truck_weights):
    answer = 0
    arrive = []
    queue = []
    num = len(truck_weights)
    bridge_weight = 0

    while len(arrive) != num:
        answer += 1
        if queue:
            if queue[0][1] == answer:
                bridge_weight -= queue[0][0]
                arrive.append(queue.pop(0))
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                bridge_weight += truck_weights[0]
                queue.append([truck_weights.pop(0), answer + bridge_length])

    return answer