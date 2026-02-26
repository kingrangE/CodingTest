"""
지도 크기 NxxM 정수로 이루어져 있음
주사위는 초기 x,y 위치에 있음
주사위는 굴러서 이동하며 아래와 같은 형태
    2
4   1   3
    5
    6
처음 상태는 윗면이 1 우측이 3 (밑 6,위 5, 아래 2, 왼 4)

주사위를 굴렸을 때, 
1. 해당 위치에 0이 있다면 주사위의 숫자를 바닥에 복사
2. 해당 위치에 0이 아닌 숫자가 있다면 숫자를 주사위에 복사

시뮬레이션으로 인식된다.
이동은 결국 4방향으로만 가능하기 때문에 이동했을 때 어떤 면이 바닥에 닿는지가 중요한 문제로 보임
< 주사위 판단법 >
윗면 = 정수
아랫면 = 정수
옆 4면 = 리스트 
내가 이동하는 방향에 따라 리스트 및 정수 업데이트가 달라짐
1. 오른쪽으로 이동
    1. 아랫면이 왼쪽면으로 변경 
    2. 왼쪽면이 윗면으로 변경
    3. 앞,뒷면은 그대로
    4. 오른쪽면이 아랫면으로 변경
    5. 윗면이 오른쪽면으로 변경
2. 왼쪽으로 이동
    1. 아랫면이 오른쪽면으로 변경
    2. 오른쪽면이 윗면으로 변경
    3. 앞,뒷면 그대로
    4. 윗면이 왼쪽면으로 변경
    5. 왼쪽면이 아랫면으로 이동
3. 아래로 이동
    1. 앞면이 아랫면으로 이동
    2. 윗면이 앞면으로 이동
    3. 뒷면이 윗면으로 이동
    4. 아랫면이 뒷면으로 이동
    5. 좌우 그대로
3. 위로 이동
    1. 앞면이 윗면으로 이동
    2. 윗면이 뒷면으로 이동
    3. 뒷면이 아래면으로 이동
    4. 아랫면이 앞면으로 이동
    5. 좌우 그대로

일단 수작업으로 쓰고, 이후에 최적화 하자.
"""

N,M,x,y,K = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]


orders = list(map(int,input().split()))

class dice :
    def __init__(self,x:int,y:int):
        # 위,아래, 앞,뒤,좌,우
        self.dices = [0,0,0,0,0,0]
        # 1~4 => 동,서,북,남 
        self.dx = [0,0,-1,1]
        self.dy = [1,-1,0,0]
        # 주사위 위치
        self.x,self.y = x,y

    def move_dice(self,order:int):
        """
        주사위 움직이고 난 뒤의 위치 (벗어나면 무효)
        """
        nx,ny = self.x+self.dx[order-1],self.y+self.dy[order-1]
        if not(0<=nx<N and 0<=ny<M) : # 벗어나면 안 움직임
            return
        self.x = nx
        self.y = ny
        if order == 1 : # 오른쪽 이동 
            self.move_right()

        elif order == 2 : #왼쪽 이동
            self.move_left()

        elif order == 3 : # 위로 이동
            self.move_up()

        else: # 아래로 이동
            self.move_down()
        
        # 움직이고 난 뒤에는 복사 및 출력
        self.copy_and_print()

    def move_right(self):
        """
        1. 아랫면이 왼쪽면으로 변경 
        2. 왼쪽면이 윗면으로 변경
        3. 앞,뒷면은 그대로
        4. 오른쪽면이 아랫면으로 변경
        5. 윗면이 오른쪽면으로 변경
        """
        self.dices[0],self.dices[1],self.dices[5],self.dices[4]=self.dices[5],self.dices[4],self.dices[1],self.dices[0]
        

    def move_left(self):
        """
        1. 아랫면이 오른쪽면으로 변경
        2. 오른쪽면이 윗면으로 변경
        3. 앞,뒷면 그대로
        4. 윗면이 왼쪽면으로 변경
        5. 왼쪽면이 아랫면으로 이동
        """
        self.dices[0],self.dices[1],self.dices[5],self.dices[4]=self.dices[4],self.dices[5],self.dices[0],self.dices[1]

    def move_up(self):
        """
        1. 앞면이 윗면으로 이동
        2. 윗면이 뒷면으로 이동
        3. 뒷면이 아래면으로 이동
        4. 아랫면이 앞면으로 이동
        5. 좌우 그대로
        """
        self.dices[2],self.dices[0],self.dices[3],self.dices[1]=self.dices[0],self.dices[3],self.dices[1],self.dices[2]
    def move_down(self):
        """
        1. 앞면이 아랫면으로 이동
        2. 윗면이 앞면으로 이동
        3. 뒷면이 윗면으로 이동
        4. 아랫면이 뒷면으로 이동
        5. 좌우 그대로
        """
        self.dices[2],self.dices[0],self.dices[3],self.dices[1]=self.dices[1],self.dices[2],self.dices[0],self.dices[3]
    def copy_and_print(self):
        if maps[self.x][self.y] == 0 :
            maps[self.x][self.y] = self.dices[1]
        else :
            self.dices[1] = maps[self.x][self.y]
            maps[self.x][self.y] = 0
        print(self.dices[0])

d = dice(x,y) 
for order in orders:
    d.move_dice(order)