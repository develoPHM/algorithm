
s = "[](){}"
from collections import deque
arr = deque(s)
cnt = 0
for i in range(len(s)):
    arr.append(arr.popleft())
    li = []
    for c in arr:
        if len(li) == 0:
            li.append(c)
            continue
        if li[-1] == '[' and c == ']':
            li.pop()
        elif li[-1] == '(' and c == ')':
            li.pop()
        elif li[-1] == '{' and c == '}':
            li.pop()
        else:
            li.append(c)
    if len(li) == 0:
        cnt += 1
print(cnt)