import sys
input = sys.stdin.readline
n = int(input())
dic ={}
for i in range(n):
    name,info = input().strip().split()
    if info == "enter":
        dic[name] = 1
    else :
        del dic[name]

for name in sorted(dic.keys(),reverse=True):
    print(name)