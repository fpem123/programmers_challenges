from collections import deque

def solution(cacheSize, cities):
    """
    answer = 0
    cashe = []
    for city in cities:
        city = city.lower()
        
        if len(cashe) == cacheSize and cashe:
            if city in cashe:
                cashe.remove(city)
                answer += 1
            else:
                cashe.pop(0)
                answer += 5
        elif len(cashe) < cacheSize and cashe:
            if city in cashe:
                cashe.remove(city)
                answer += 1
            else:
                answer += 5
        else:
            answer += 5
        
        cashe.append(city)
        """
    answer = 0
    cashe = deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.lower()
        
        if city in cashe:
            answer += 1
            cashe.remove(city)
            cashe.append(city)
        else:
            answer += 5
            cashe.append(city)
    
    return answer