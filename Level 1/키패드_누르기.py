def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    key_pad = {1:(0, 0), 2:(0, 1), 3:(0, 2),
              4:(1, 0), 5:(1, 1), 6:(1,2),
              7:(2,0), 8:(2,1), 9:(2,2),
              '*': (3,0), 0:(3,1), '#':(3,2)}
    left_pos = key_pad['*']
    right_pos = key_pad['#']

    for number in numbers:
        
        if number in left:
            answer += 'L'
            left_pos = key_pad[number]
        elif number in right:
            answer += 'R'
            right_pos = key_pad[number]
        else:
            num_pos = key_pad[number]
            
            left_len = abs(left_pos[0] - num_pos[0]) + abs(left_pos[1] - num_pos[1])
            right_len = abs(right_pos[0] - num_pos[0]) + abs(right_pos[1] - num_pos[1])
            
            if left_len < right_len:
                answer += 'L'
                left_pos = key_pad[number]
            elif left_len > right_len:
                answer += 'R'
                right_pos = key_pad[number]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = key_pad[number]
                else:
                    answer += 'R'
                    right_pos = key_pad[number]
                    

    return answer