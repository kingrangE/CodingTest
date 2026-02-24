"""
배열이 주어진다.

배열에 있는 각 값이 특정 값보다 작으면 이용 불가함.
특정 값보다 작지 않은 경우 이용이 가능하고, 이것이 4면 중 하나이상 붙어있지 않으면 독립적으로 판단

독립적인 구역의 개수가 가장 많을 때의 특정 값을 구하라.

배열의 최대, 최소값을 먼저 구함.

Q) 모든 반복을 하지 않고, 최대/최소를 구하는 방법이 존재하는가?
A) 없다.
=> 따라서, 최솟값부터 최대값까지 반복하며 확인하는 것이 정석으로 보인다.

pseudo
for (최소~최데):
    각 부분을 탐색하며, 독립된 부분의 개수 파악
    최대값 갱신

계속 BFS로 풀었으므로, 이번엔 DFS로 풀어보자 -> 주석 처리한 것처럼 풀었는데 recursion Error뜸 
"""
from copy import deepcopy

N = int(input())

# def dfs(map:list,i:int,j:int,depth:int):
#     if 0<=i<N and 0<=j<N and map[i][j] > depth:
#         map[i][j] = depth
#         dfs(map,i+1,j,depth)
#         dfs(map,i-1,j,depth)
#         dfs(map,i,j+1,depth)
#         dfs(map,i,j-1,depth)

def dfs(map:list,i:int,j:int,depth:int):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    stack = []
    stack.append((i,j))
    map[i][j] = depth
    while stack:
        x,y = stack.pop()
        for mx,my in zip(dx,dy):
            nx,ny = mx+x,my+y
            if 0<=nx<N and 0<=ny<N and map[nx][ny] > depth:
                map[nx][ny] = depth
                stack.append((nx,ny))

map = [list(map(int,input().split())) for _ in range(N)]

min_val = float('inf')
max_val = -1
# 최대 최소 파악하기 (O(N^2)) -> 최악 : 10,000회 
for row in map:
    for val in row:
        if val < min_val : 
            min_val = val
        if val > max_val :
            max_val = val


result = 1
# 반복하며 DFS
for depth in range(min_val,max_val):
    # 최소  ~ 최대 반복
    count = 0
    copy_map = deepcopy(map)
    for i in range(len(map)):
        for j in range(len(map[i])) :
            if copy_map[i][j] > depth: #가라앉지 않는 지역 찾음
                dfs(copy_map,i,j,depth)
                count+=1
    
    result = max(count,result)
print(result)