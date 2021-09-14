from itertools import combinations

def solution(info, query):
    answer = []
    infoDict = {}
    
    for i in info:
        i = i.split()
        
        for idx in range(5):
            x = list(combinations(i[:-1], idx))
            
            for y in x:
                infoDict.setdefault("".join(y), []).append(int(i[-1]))
    
    for item in infoDict.values():
        item.sort()
    
    for queryPiece in query:
        queryPiece = queryPiece.replace('and', '').replace("-", "").split()
        cutLine = int(queryPiece[-1])
        queryPiece = "".join(queryPiece[:-1])
        
        try:
            target = infoDict[queryPiece]
            start = 0
            end = len(target)
            mid = (start + end) // 2

            while start <= end:
                mid = (start + end) // 2

                if target[mid] < cutLine:
                    start = mid + 1
                else:
                    end = mid - 1

            answer.append(len(target) - start)
        except:
            answer.append(0)
    
    return answer