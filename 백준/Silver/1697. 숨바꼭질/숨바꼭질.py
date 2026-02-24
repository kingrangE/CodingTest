"""
수빈이 위치 N
동생 위치 K
수빈이는 항상 자신의 위치에서 X-1 / X+1 / 2*X 중 하나로 이동 가능
수빈이가 동생 위치까지 도달하는 가장 짧은 시간

수빈의 위치와 거기까지 도달하는데 걸린 시간을 Queue에 넣고
큐가 빌 때까지 반복해서 동생 위치에 도달하는데 걸린 가장 짧은 시간을 체크한다.
# 만나자마자 종료가 가능한ㄱ가? 예외는 없는가?

가능하다. BFS로 하면, 동일 시간에 갈 수 있는 가장 짧은 위치가 항상 저장되기 때문에
동일한 반복에서 항상 가장 짧은 시간임을 보장한다.

는 메모리 초과

----
배열을 써서 해결하자 (한 번 갔던 곳은 다시 방문할 필요 X -> 항상 이전에 도착한게 최소 횟수이기 때문)
"""
from collections import deque

q = deque()
N,K = map(int,input().split())
visited = [0 for _ in range(100001)]
if N == K :
    print(0)
else:
    q.append(N)
    while q : 
        now = q.popleft()
        for next in [now+1,now-1,now*2]:
            
            if 0<=next<=100000 and visited[next] == 0 :
                # 방문 안했고 유효 범위면 기록
                visited[next] = visited[now]+1
                q.append(next)
            if next == K : 
                print(visited[now]+1)
                exit()