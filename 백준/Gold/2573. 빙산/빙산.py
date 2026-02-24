"""
빙하가 두덩이로 나눠지는 최소 시간을 구하라.
만약 분리 안되면 0 출력
O(N*M)반복하며 빙하 상태 갱신
BFS로 빙하 개수 세기 (2면 종료)
2개 안되고 끝나면 종료

pseudo


"""
from collections import deque
from copy import deepcopy

N,M = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def decrease_glacier(i,j): # 최악의 경우 360000회 (안전 범위)
    for mx,my in zip(dx,dy):
        nx,ny = i+mx, j+my
        if 0<=nx<N and 0<=ny<M and maps[nx][ny] > 0:
            # 빙하면 줄이기
            maps[nx][ny] -= 1

def check_zero()->bool: # 최악의 경우 90000회
    for row in maps:
        for val in row:
            if val > 0 : # 빙하 있는 곳있으면 트루
                return True
    return False

def bfs(map:list,i:int,j:int):
    from collections import deque
    q = deque()
    map[i][j] = 0
    q.append((i,j))
    while q :
        x,y = q.popleft()
        for mx,my in zip(dx,dy):
            nx,ny = mx+x,my+y
            if 0<=nx<N and 0<=ny<M and map[nx][ny] > 0:
                map[nx][ny] = 0
                q.append((nx,ny))

year = 0
while check_zero() : # 1회 반복 최악 개수 -> 450000회 + 약 360000 -> 100만 -> 20번만 해도 시간 초과 (but, 값이 10이하라 ㄱㅊ)
    # 빙하 개수 체크 
    copy_map = deepcopy(maps)
    count = 0
    for i in range(N):
        for j in range(M):
            if copy_map[i][j] > 0: # 빙하 찾음
                bfs(copy_map,i,j) # 빙하 붙어있는 애들 검사
                count+=1 # 빙하 덩어리 개수 추가

    if count >= 2: # 두 덩이면
        print(year)
        exit()

    year += 1
    copy_map = deepcopy(maps)

    # 빙하 감소
    for i in range(N):
        for j in range(M):
            if copy_map[i][j] == 0 :
                decrease_glacier(i,j)
    
print("0")