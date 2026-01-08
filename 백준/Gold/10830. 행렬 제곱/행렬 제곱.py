"""
행렬 A의 B제곱을 구하라
이때, A^B의 각 원소를 1000으로 나눈 나머지를 출력

- 제곱이고 B가 매우 크므로(<100억?정도), 그냥 돌리면 안된다.
- 제곱 수의 곱은 +이다.
    - 예를 들어, 100 제곱을 구해야 한다는 아래와 같다.
        1. 50제곱 + 50제곱
        2. 25제곱 + 25제곱
        3. 12제곱 + 13제곱
        4. 6제곱 + 6제곱 / 6제곱 + 7제곱
        5. 3제곱 + 3제곱 / 3제곱 + 4제곱
        6. 1제곱 , 2제곱, 3제곱 구하기
"""

import math
N, B = map(int,input().split())
maps = [list(map(lambda x : x%1000,map(int,input().split()))) for _ in range(N)]

square_map = {1:maps} # index : 리스트 (ex, 1제곱 : [], 2제곱 : [])

def recur(n : int):
    if n in square_map.keys():
        return square_map[n]
    tmp1 = math.ceil(n/2)
    tmp2 = math.floor(n/2)
    square_map[n] = multiply(recur(tmp1),recur(tmp2))
    return square_map[n]
    

def multiply(map1:list,map2:list):
    map2 = transform(map2)
    result = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(mul_list(map1[i],map2[j])%1000)
        result.append(tmp)
    return result

def transform(map:list)->list:
    return list(zip(*map))

def mul_list(l1:list,l2:list)->int:
    result= 0
    for i,j in zip(l1,l2):
        result+= i*j
    return result

for i in recur(B):
    print(*i,sep=" ")