from collections import deque
def solution(priorities, location):
    names = [ chr(65+idx) for idx in range(len(priorities))]
    target = names[location]
    dic = { name:priority for name,priority in zip(names,priorities)}

    priority_queue = deque(priorities)
    name_queue = deque(names)
    count = 0
    while True:
        max_p = max(dic.values())
        while True:
            p = priority_queue.popleft()
            n = name_queue.popleft()
            if p == max_p :
                if n == target : 
                    return count + 1
                dic.pop(n)
                break
            priority_queue.append(p)
            name_queue.append(n)
        count += 1