import re
from collections import Counter

def intersection(data1, data2):
    intersectionSize = 0
    data1 = dict(Counter(data1))
    data2 = dict(Counter(data2))
    
    for item in data1:
        if item in data2:
            while data1[item] != 0 and data2[item] != 0 :
                data1[item] -= 1
                data2[item] -= 1
                intersectionSize += 1
    
    return intersectionSize


def setMaker(data):
    resultSet = []
    data = data.lower()
    
    for idx in range(len(data) - 1):
        item = data[idx] + data[idx + 1]
        
        if re.search('[^a-z]', item):
            continue
        
        resultSet.append(item)
    
    return resultSet


def solution(str1, str2):
    answer = 0
    str1Set = setMaker(str1)
    str2Set = setMaker(str2)
    intersectionSize = intersection(str1Set, str2Set)
    unionSize = len(str1Set) + len(str2Set) - intersectionSize
    
    if unionSize == 0:
        return 65536
    
    answer = int(65536 * (intersectionSize / unionSize))
    
    return answer