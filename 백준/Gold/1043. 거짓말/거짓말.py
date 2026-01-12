"""
1751
입력 :
사람의 수 N / 파티의 수 M
진실을 아는 사람의 수 및 번호
M개의 줄 동안 파티에 오는 사람 수와 번호

진실을 아는 사람이 파티에 오면 그 때 참가한 모든 사람은 진실을 아는 사람으로 변경
진실을 아는 사람이 없다면 result += 1
최대 개수 출력

---- 2번째 IDEA ----
(첫번쨰는 나중에 들은 사람도 치면 안된다는 규칙에 틀림(안써있어놓고 어렵게 할라고 억지부림))
1 1
2 2 3
2 3 4
2 4 5
2 6 7
2 8 9
2 1 2
0
각 번호 별로 party에서 만난 사람을 저장함. (O(M))
위의 경우
1 : 1,2
2 : 1,2,3
3 : 2,3,4
4 : 3,4,5
5 : 4,5
6 : 6,7
7 : 6,7
8 : 9,8
9 : 8,9
이 상태에서 하나씩 key를 꺼내서 queue에 넣음 O(N)
[2]
[3]
[4]
[5]
[]
더이상 반복 못함
해당 값들을 모두 set에 넣고 몇 개나 ㄱㅊ은지 다시 셈 (O(N))
"""
from collections import deque

N,M = map(int,input().split())
q = deque() # 큐
met = {} #만남 사람 기록
truth_set = set()
truth_group = list(map(int,input().split()))[1:]
parties = [list(map(int,input().split()))[1:] for _ in range(M)]
result = 0
for party in parties :
    for p in party:
        now = met.get(p,[])
        now.extend(party) 
        met[p] = now # 전체를 다 등록

q.extend(truth_group)
while q : #q가 빌때까지
    num = q.popleft()
    truth_set.add(num)
    met_list = met.get(num,[]) # 만난 사람들
    # print(q,num,met_list)
    for people in met_list:
        if truth_set.__contains__(people) : #이미 진실을 아는 사람이면 패스
            continue
        truth_set.add(people)
        q.append(people) #진실을 이제 안 사람 추가
# print(truth_set)
for party in parties :
    if(set(party) & truth_set) :
        #교집합 있으면 패스
        continue
    result+=1 #교집합 없으면 구라 ㄱㄱ

print(result)
"""첫 시도 코드"""
# truth_group = set(list(map(int,input().split()))[1:])
# result = 0
# parties = []
# for i in range(M):
#     parties.append(set(list(map(int,input().split()))[1:]))

# for party in parties :
#     if (truth_group & party) :
#         # 교집합 존재 : 진실 그룹 확장
#         truth_group = truth_group | party
#     else :
#         result += 1
# print(result)
