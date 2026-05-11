from collections import Counter

def solution(participant, completion):
    dict = {}
    
    for name in participant:
        if name in dict:
            dict[name] += 1
        else:
            dict[name] = 1
    
    for name in completion:
        dict[name] -= 1
    
    for name in dict:
        if dict[name] >= 1:
            return name