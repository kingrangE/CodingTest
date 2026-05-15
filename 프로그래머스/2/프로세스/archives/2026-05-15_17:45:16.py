def solution(p,l):
    arr = [(i,p) for i,p in enumerate(p)]
    answer = 0
    
    while arr:
        cur = arr.pop(0)
        if any([cur[1] < other[1] for other in arr]) :# 다른 것들 중에 큰게 하나라도 있으면 다시 넣어
            arr.append(cur)
        else : # 이게 가장 큰거면 넣을 필요 없음
            answer += 1
            if cur[0] == l : # 목표 위치와 맞으면
                break
            
    
    return answer