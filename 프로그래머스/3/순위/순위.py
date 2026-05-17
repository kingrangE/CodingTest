"""
단방향 그래프 2개 (이김, 짐)

이기고 지는 것을 BFS (예를 들어, 내가 A한테 이기고 A가 B를 이긴다면 나는 B도 이기는거임)로 탐색해서 상대 순위가 결정되는 인원수를 파악

파악한 인원 수가 전체와 같다면 순위가 결정되는거
"""
from collections import deque
def bfs(graph,start):
    q = deque([start])
    visited = [start]
    while q:
        now = q.popleft()
        for neighbors in graph[now]:
            # 연결된 노드들 중 방문 안한거 추가
            if neighbors not in visited :
                visited.append(neighbors)
                q.append(neighbors)
    return len(visited)-1 # 자기 자신 빼기

def solution(n, results):
    answer = 0
    win_graph = [[] for _ in range(n+1)]
    lose_graph = [[] for _ in range(n+1)]
    
    for win,lose in results :
        win_graph[win].append(lose)
        lose_graph[lose].append(win)
    
    for i in range(1,n+1):
        # 각 노드들에 대해 수행
        if (bfs(win_graph,i) + bfs(lose_graph,i) == n-1) :
            answer += 1    
    
    return answer