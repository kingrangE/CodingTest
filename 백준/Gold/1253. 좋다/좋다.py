"""
N개의 수 중 두 수를 더해 좋은 수 구하기

1. for 문으로 하나씩 값이랑 인덱스 가져오기
2. 이분 탐색으로 해결하기
3. for i,e in enumerate(arr):
       for idx in range(i):
           # 값을 하나 고정
           # start 
           # end 로 탐색
"""

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 0
for idx,num in enumerate(arr) : 
    start = 0
    end = len(arr)-1
    while start < end:
        if start == idx:
            start+=1 #건너뛰기
            continue
        if end == idx :
            end -= 1
            continue
        if arr[start]+arr[end] == num :
            result+=1 
            break
        elif arr[start]+arr[end] < num :
            start+=1
        else : 
            end -= 1
        
        
print(result)