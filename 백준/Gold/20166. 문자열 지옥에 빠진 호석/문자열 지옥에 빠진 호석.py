"""
1. 왔던 곳 다시가기 가능
2. 전방향 이동 가능(대각선 포함)
3. 시작하는 알파벳을 시작으로 이동할때마다 이어붙여서 단어 만들기 가능
4. 주어진 문자열 K개를 만들 수 있는 각 경우의 수를 반환
5. 방문 순서가 다르면 다른 경우
"""
import sys
from collections import deque

def bfs(x:int,y:int,target:str) -> int:
    if not target.startswith(maps[x][y]): 
        # 시작 단어가 다르면 만들 수 없음
        return 0
    
    q = deque()
    q.append((x,y,maps[x][y])) #(x,y) , substring
    dx = [1,1,1,-1,-1,-1,0,0]
    dy = [1,-1,0,1,-1,0,1,-1]
    count = 0

    while q :
        now_x,now_y,substring = q.popleft()
        if substring == target.strip() :
            count+=1 # 찾았으면 개수 더하고
            continue # 다음 반복
        for mx,my in zip(dx,dy):
            nx,ny = adjust(now_x+mx,N),adjust(my+now_y,M)
            new_string = substring + maps[nx][ny]
            if len(new_string) <= len(target.strip()) and target.strip().startswith(new_string):
                q.append((nx,ny,new_string))
    # print()
    return count

def adjust(now,maximum) :
    if now > maximum-1 :
        return 0
    if now < 0 :
        return maximum-1
    return now

input = sys.stdin.readline

N,M,K = map(int,input().split())

maps = [list(input()) for _ in range(N)]

words = [input() for _ in range(K)]
dic = {}

for word in words :
    count = 0
    if word not in dic :
        for i in range(N):
            for j in range(M):
                count += bfs(i,j,word)
        dic[word]=count
    print(dic[word]) 