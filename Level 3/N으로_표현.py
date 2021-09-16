def solution(N, number):
    number_dict = dict()
    tmp = 0
    
    for i in range(0, 8):
        tmp += pow(10, i) * N
        number_dict[i + 1] = {tmp}
    
    for step in range(1, 9):
        for runner in range(1, step):
            for pick_1 in number_dict[runner]:
                for pick_2 in number_dict[step - runner]:
                    number_dict[step].add(pick_1 + pick_2)
                    number_dict[step].add(pick_1 - pick_2)
                    number_dict[step].add(pick_1 * pick_2)
                    if pick_2 != 0:
                        number_dict[step].add(pick_1 // pick_2)
                    
        if number in number_dict[step]:
            return step
    else:
        return -1
    
    
    return answer