def solution(s):
    answer = True
    open = 0
    for i in range(len(s)):
        if (s[i] == '(') :
            open += 1
        elif (s[i] == ')') :
            open -= 1
            if open < 0:
                return False
    if open > 0:
        return False
    return True