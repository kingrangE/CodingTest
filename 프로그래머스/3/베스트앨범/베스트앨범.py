def solution(genres, plays):
    
    answer = []
    total_dic = {}
    count_dic = {}
    for i in range(len(genres)):
        if genres[i] not in total_dic :
            total_dic[genres[i]] = plays[i]
            count_dic[genres[i]] = [(plays[i],i)]
        else :
            total_dic[genres[i]] += plays[i]
            count_dic[genres[i]].append((plays[i],i))
            
    result = [(play,genre) for genre,play in total_dic.items()]
    result.sort(reverse=True)
    
    for _,g in result :
        # play가 높은거부터 나옴
        count_dic[g].sort(key=lambda x: (x[0],-x[1]),reverse=True)
        answer.extend([i for _,i in count_dic[g][:2]])  #앞에서부터 2개
    
    return answer