import sys
import heapq
N,M = map(int,input().split())
heap = list(map(int,input().split()))
heapq.heapify(heap)
for i in range(M):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap,a+b)
    heapq.heappush(heap,a+b)

print(sum(heap))