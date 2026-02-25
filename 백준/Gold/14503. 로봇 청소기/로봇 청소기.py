"""
시뮬레이션

로봇 청소기는 다음과 같이 작동한다.

현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
현재 칸의 주변 
$4$칸 중 청소되지 않은 빈 칸이 없는 경우,
바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
현재 칸의 주변 
$4$칸 중 청소되지 않은 빈 칸이 있는 경우,
반시계 방향으로 
$90^\circ$ 회전한다.
바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
1번으로 돌아간다.

왼쪽 서쪽 오른쪽 동쪽 위 북 아래 남
로봇 청소기 위치랑 보는 방향 제공 (0,1,2,3)(북,동,남,서)

하라는 대로 구현해서 청소한 칸의 수 반환하기
"""

N,M = map(int,input().split())
r,c,d = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]

# d와 맞춰서 작성 (0,1,2,3)(북,동,남,서)
dx = [0,1,0,-1]
dy = [-1,0,1,0]

def check_around() :
    for i in range(4):
        nr, nc = r+dy[i], c+dx[i]
        if 0<= nr < N and 0<=nc<M and maps[nr][nc]== 0 :
            # 청소 안된 곳 있으면
            return True
    # 없으면 
    return False

tiles = 0 # 청소한 타일
while True:
    if maps[r][c]!=2 :
        maps[r][c] = 2 # 청소 표시
        tiles += 1
    # print(*maps,sep="\n")
    # print()
        
    if check_around():
        # 주변에 청소 안된 곳 있나 확인
        for i in range(1,5):
            nr, nc = r+dy[d-i], c+dx[d-i]
            now = maps[nr][nc]
            if 0<= nr < N and 0<=nc<M and now == 0 :
                # 반시계 돌렸더니 청소 안한 위치 찾음
                if d-i<0 :
                    d = 4+(d-i)
                else :
                    d = d-i
                r,c = nr,nc  # 위치 갱신 (어차피 반복 시작할 때 청소함)
                break
    else :
        # 기본은 앞으로 가는거니까 반대방향으로 가야함 (따라서 -2)
        nr,nc = r+dy[d-2],c+dx[d-2]
        if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] != 1:
            # 갈 수 있는 위치면 업데이트
            r,c = nr,nc 
        else :
            # 갈 수 없으면 종료
            print(tiles)
            exit()
