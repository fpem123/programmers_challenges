from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    """
    for i in course:
        orderDict = {}
        hightstMenuList = []
        hightsOrderCount = 0
        
        for order in orders:
            order = sorted(order)
        
            for combination in list(combinations(order, i)):
                combination = "".join(combination)
                orderDict.setdefault(combination, 0)
                orderDict[combination] += 1
    
        for candidate in orderDict.keys():
            if orderDict[candidate] > 1:
                if orderDict[candidate] > hightsOrderCount:
                    hightsOrderCount = orderDict[candidate]
                    hightstMenuList = [candidate]
                elif orderDict[candidate] == hightsOrderCount:
                    hightstMenuList.append(candidate)
        
        answer += hightstMenuList
    """
    for i in course:
        orderPieceList = []
        biggerOrderNumber = 0
        
        for order in orders:
            order = sorted(order)
        
            for combination in list(combinations(order, i)):
                orderPieceList.append("".join(combination))
    
        orderPieceList = Counter(orderPieceList).most_common()
        
        for menu in orderPieceList:
            if menu[1] > 1 and menu[1] == orderPieceList[0][1]:
                answer.append(menu[0])
    
    return sorted(answer)