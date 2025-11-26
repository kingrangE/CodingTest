"""
1. 버튼을 누른 순서대로 대기목록에 들어감
2. 대기열 -> 수강신청 -> 맨 뒤로
3. 수강신청 비활성화 -> 앞에서부터 수강신청, 꽉차면 나머지 무시 후 종료
"""
import sys

input = sys.stdin.readline
K,L = map(int,input().split())
users = {}
for i in range(L):
    id = input().strip()
    users[id] = i
# print(users)
sorted_users = sorted(users.items(),key=lambda x: x[1])
for i in range(min(K,len(sorted_users))):
    print(sorted_users[i][0])