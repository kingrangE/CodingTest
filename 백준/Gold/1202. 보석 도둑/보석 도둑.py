import heapq
import sys

# 입력 속도를 높이기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

N, K = map(int, input().split())

# 보석 정보: [무게, 가치] (무게 기준 오름차순 정렬)
jewelries = []
for _ in range(N):
    heapq.heappush(jewelries, list(map(int, input().split())))

# 가방 용량 (오름차순 정렬)
bags = sorted([int(input()) for _ in range(K)])

result = 0
candidate_jewels = [] # 현재 가방에 담을 수 있는 보석들 (최대 힙)

# 1. 가방을 하나씩 확인 (작은 가방부터)
for bag_capacity in bags:
    
    # 2. 현재 가방에 '담을 수 있는' 모든 보석을 후보군에 추가
    #    (무게가 가벼운 보석부터 확인)
    while jewelries and jewelries[0][0] <= bag_capacity:
        # jewelries[0][0]은 가장 가벼운 보석의 무게
        weight, value = heapq.heappop(jewelries)
        
        # '가치'를 기준으로 최대 힙에 저장 (heapq는 최소 힙이므로 -value)
        heapq.heappush(candidate_jewels, -value)
        
    # 3. 후보군에 보석이 있다면
    if candidate_jewels:
        # 4. 후보 중 '가장 비싼' 보석을 꺼내 가방에 담음 (결과에 더함)
        #    (-value로 넣었으니, 다시 -를 붙여 원래 가치로 환원)
        result += -heapq.heappop(candidate_jewels)

print(result)