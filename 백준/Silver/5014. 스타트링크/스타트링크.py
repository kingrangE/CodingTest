from collections import deque

F,S,G,U,D = map(int,input().split())

if F < G :
    print("use the stairs")
    exit()
if S == G:
    print("0")
    exit()

q = deque()
q.append(S)
visited = [-1 for _ in range(F+1)]
visited[S] = 0
while q : 
    now = q.popleft()
    for next in [now+U,now-D]:
        if 1 <= next <= F:
            if next == G :
                print(visited[now]+1)
                exit()
            elif visited[next] == -1:
                q.append(next)
                visited[next] = visited[now]+1
print("use the stairs")