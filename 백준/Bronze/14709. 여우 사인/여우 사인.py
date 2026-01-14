
"""
마라톤 급수 올리려고 푸는 문제
"""
fox = {(1,3),(3,1),(4,3),(3,4),(1,4),(4,1)}
hands = set()

for _ in range(int(input())):
    tmp = tuple(map(int,input().split()))
    hands.add(tmp)
if len(hands - fox) == 0 and len(hands)>=3:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else :
    print("Woof-meow-tweet-squeek")