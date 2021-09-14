def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            """
            number = number + ((number ^ (number + 1)) + 1) // 4
            answer.append(number)
	"""
            number = '0' + format(number, 'b')
            zeroneIdx = number.rfind('01')
            number = list(number)
            number[zeroneIdx] = '1'
            number[zeroneIdx + 1] = '0'
            number = "".join(number)
            number = int(number, 2)
            answer.append(number)
    
    return answer