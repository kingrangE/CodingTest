"""
마라톤 급수 올리려고 푸는 문제
"""
items= [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
alpha_dic = {}
for i in range(len(items)):
    alpha_dic[chr(i+65)] = items[i]

string = input()
result = 0
for s in string:
    result +=alpha_dic[s]
if result%2 == 0 :
    print("You're the winner?")
else : 
    print("I'm a winner!")