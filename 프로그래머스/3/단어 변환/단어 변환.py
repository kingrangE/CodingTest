from collections import deque

def diff_count(word1,word2):
    diff = 0
    for a,b in zip(word1,word2):
        if a!= b :
            diff += 1
        if diff > 1:  # 조기 종료
            return diff 
    return diff

def solution(begin, target, words):
    if target not in words: # 타겟이 없으면 불가
        return 0
    q = deque()
    visited = []
    q.append((begin,0))
    while q : 
        now_word,count = q.popleft()
        if now_word == target :
            return count
        for word in words:
            if word not in visited and diff_count(word,now_word) == 1:
                q.append((word,count+1))
                visited.append(word)
    return 0