from collections import deque

N = int(input())
result = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i:int,j:int):
    q = deque()
    q.append((i,j))
    cnt = 0
    while q :
        x,y = q.popleft()
        if map[x][y] == 0:
            continue
        map[x][y] = 0
        cnt+=1
        for mx,my in zip(dx,dy):
            nx,ny = x+mx,y+my
            if 0 <= nx < N and 0 <= ny < N and map[nx][ny] != 0 :
                q.append((nx,ny))

    result.append(cnt)

map = [list(map(int,list(input()))) for _ in range(N)]

count = 0 

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 :
            count+= 1
            bfs(i,j)

print(count)
result.sort()
print(*result,sep="\n")