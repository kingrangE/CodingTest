from collections import Counter
def solution(nums):
    c = Counter(nums)
    unique_nums = list(c.keys())
    
    return min(len(unique_nums),len(nums)//2)