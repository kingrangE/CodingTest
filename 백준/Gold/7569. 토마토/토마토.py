"""
상자의 크기 M,N,H 

토마토는 익은토마토와 상하좌우,앞,뒤 로 인접한 경우 익는다.

모든 토마토가 다 익을라면 얼마나 걸리나

모두 익음 -> 0
모두 익지 못하면 -> -1

일반적인 BFS문제에서 상하 라는 조건이 추가된 것이다.
"""
from collections import deque

q = deque()
M,N,H = map(int,input().split())
boxes = []
for _ in range(H):
    boxes.append([list(map(int,input().split())) for _ in range(N)])

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

# 익은 토마토들 위치 파악 O(N^3) -> 100^3 = 10000000 (<20000000)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1 : # 토마토 있으면
                q.append((i,j,k,0)) # 아직 1일 안지남

max_day = 0
while q :
    x,y,z,day = q.popleft()
    max_day = max(day,max_day)
    for mx,my,mz in zip(dx,dy,dz):
        nx, ny, nz = mx+x, my+y, mz+z
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and boxes[nx][ny][nz] == 0: 
            # 유효 범위 + 안익은 토마토 => 익게하고 추가
            boxes[nx][ny][nz] = 1
            q.append((nx,ny,nz,day+1))
    


# 안 익은 토마토 존재 파악 -> 있으면 -1
for box in boxes:
    for row in box:
        for val in row:
            if val == 0 :
                print("-1")
                exit()

print(max_day)