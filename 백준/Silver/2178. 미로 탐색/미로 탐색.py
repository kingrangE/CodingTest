from collections import deque
from copy import deepcopy


N,M = map(int,input().split())

map = [list(map(int,list(input())))for i in range(N)]

q = deque()

q.append((0,0))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0
while q :
    x,y = q.popleft()
    for mx,my in zip(dx,dy):
        nx,ny = mx+x,my+y
        if 0 <= nx < N and 0 <= ny < M and map[nx][ny] == 1: # 유효 범위 이내고 더 적은 이동횟수면
            #추가
            map[nx][ny] = map[x][y]+1
            q.append((nx,ny))

print(map[N-1][M-1])
