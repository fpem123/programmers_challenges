import heapq

def solution(scoville, K):
    answer = 0
    hq = []
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        answer += 1
        newFood = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, newFood)
    
    return answer