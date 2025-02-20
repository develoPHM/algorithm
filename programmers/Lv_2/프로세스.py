from collections import deque
def solution(priorities, location):
    arr = priorities[::]
    arr.sort()
    ans = 0
    for i in range(len(priorities)):
        priorities[i] = [priorities[i], i]
    li = deque(priorities)
    while True:
        bigger = arr.pop()
        check = li.popleft()
        if check[0] == bigger:
            ans += 1
            if check[1] == location:
                break
        else:
            li.append(check)
            arr.append(bigger)
    return ans