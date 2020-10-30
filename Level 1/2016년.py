def solution(a, b):
    answer = ''
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = sum(months[:a - 1]) + b - 1
    
    answer = week[day % 7]
    
    return answer
    
    '''
    answer = 'FRI'
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month = 1
    day = 1
    
    while True:
        if month == a and day == b:
            break
            
        day += 1
        answer = week[(week.index(answer) + 1) % 7]
        
        if month == 2 and day == 30:
            month += 1
            day = 1       
        if month < 8 and month % 2 == 0 and day == 31:
            month += 1
            day = 1
        if month < 8 and month % 2 == 1 and day == 32:
            month += 1
            day = 1
        if month > 7 and month % 2 == 0 and day == 32:
            month += 1
            day = 1
        if month > 7 and month % 2 == 1 and day == 31:
            month += 1
            day = 1
    '''
        
    return answer