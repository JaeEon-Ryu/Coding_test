import heapq  # function for sort

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # conversion to heap structure

    while scoville[0] < K:  # repeat until scoville number
        if len(scoville) < 2:
            return -1
        else:
            newNum = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville, newNum)
            answer += 1

    return answer