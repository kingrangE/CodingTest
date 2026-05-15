from collections import defaultdict
def solution(clothes):
    dic = defaultdict(int)
    
    for c in clothes:
        dic[c[1]] += 1
    
    values = list(dic.values())
    answer = 0
    
    for i in range(len(values)):
        count = values[i]
        for j in range(i+1,len(values)):
            count *= values[j]+1
        answer += count
    
    return answer