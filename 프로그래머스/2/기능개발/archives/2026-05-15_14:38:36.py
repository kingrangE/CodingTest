def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    total = 0
    while count < len(progresses):
        day+=1
        
        for i in range(count, len(progresses)):
            if progresses[count] + day*speeds[count] >=100 :
                count+=1
        if total != count:
            answer.append(count-total)
            total = count    
            
    
    return answer