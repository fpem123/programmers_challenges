from collections import Counter

def solution(citations):
    answer = 0
    size = len(citations) + 1
    
    citations = list((Counter(citations)).items())
    citations.sort(key = lambda x: x[0])

    for h in range(size):
        s = 0
        for citation in citations:
            if citation[0] >= h:
                s += citation[1]
        
        if h <= s:
            answer = h

    
    return answer