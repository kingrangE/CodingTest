"""
BFS로 첫 노드부터 방문
방문한 노드는 visited에 담음
방문하지 않은 노드들을 for문으로 반복해서 방문하며, result+=1
"""
from collections import deque

def solution(n, computers):
    visited = [0 for _ in range(n)]
    answer = 0
    
    for i in range(n):
        if visited[i] == 1: # 방문한 노드면 이미 BFS 돌았음
            continue
        q = deque()
        q.append(i)
        while q :
            current_node = q.popleft()
            visited[current_node] = 1
            for new_node,value in enumerate(computers[current_node]):
                # 현재 노드와 연결된 노드들을 정보를 가져옴
                if visited[new_node] == 0 and value == 1 :
                    q.append(new_node) # 방문 안하고, 연결되어 있으면 큐에 추가 다음 번에 탐색   
        answer += 1
    return answer