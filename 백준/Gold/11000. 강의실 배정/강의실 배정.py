import sys
import heapq
input = sys.stdin.readline

N = int(input())

lecture = [list(map(int,input().split())) for _ in range(N)]
lecture.sort(key = lambda x: (x[0],x[1])) # 앞에 값을 기준으로 정렬함
class_room = [lecture[0][1]]

for idx in range(1,N):
    if class_room[0] <= lecture[idx][0] :
        # 갱신 가능
        heapq.heappop(class_room)
    heapq.heappush(class_room,lecture[idx][1])

print(len(class_room))