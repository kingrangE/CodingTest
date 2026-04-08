"""
스코빌 지수 = 가장 안 맵 + 가장 2번쨰 안 맵 *2
섞어야 하는 최소 횟수를 구하라.

최소니까 그리디라고 생각할 수 있지만, 계속해서 "가장" 뒤에서 두 개를 계속 빼는 것이므로 heap을 사용한다.
"""
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>1:
        min_1=heapq.heappop(scoville)
        if min_1 >= K :
            # 가장 작은게 K이상이면 다 이상인거
            break
        min_2=heapq.heappop(scoville)
        
        new_s = min_1 + min_2 * 2
        heapq.heappush(scoville,new_s)
        answer+=1
    if len(scoville) == 1 and scoville[0] < K :
        return -1
    return answer