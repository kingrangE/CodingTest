import bisect
def solution(n_str):
    if n_str[0] != '0':
        return n_str
    
    answer = n_str[bisect.bisect_right(list(n_str),'0'):]
    return answer