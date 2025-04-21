from collections import deque
N = int(input())
num = list(range(1, N + 1))
paper = list(map(int,input().split()))
li = deque()
ans = [] # 답
for i in range(N):
    li.append([num[i], paper[i]])

while len(li) > 1:
    point = li.popleft()
    ans.append(point[0])
    if point[1] == 1:
        continue
    if point[1] > 1:
        for _ in range((point[1] - 1) % len(li)):
            li.append(li.popleft())
    if point[-1] < 0:
        if point[-1] == -1:
            li.appendleft(li.pop())
        else:
            for _ in range(abs(point[-1]) % len(li)):
                li.appendleft(li.pop())
ans.append(li[0][0])
print(*ans)