
"""
마라톤 급수 올리려고 푸는 문제
"""
A,B = map(int,input().split())
A_r = int("".join(["1" for _ in range(A)]))
B_r = int("".join(["1" for _ in range(B)]))

print(A_r+B_r)
