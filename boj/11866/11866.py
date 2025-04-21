from collections import deque

N, K = map(int, input().split())
table = deque(range(1, N + 1))
ans = []
while len(table) > 1:
    for _ in range(K - 1):
        table.append(table.popleft())
    ans.append(table.popleft())
ans.append(table.popleft())
for i in range(len(ans)):
    ans[i] = str(ans[i])
print('<'+', '.join(ans)+'>')