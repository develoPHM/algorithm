from collections import deque

N, K = map(int, input().split())
max_cnt = 100000


def bfs(n):
    v = [False] * (max_cnt + 1)
    q = deque([[n, 0]])
    v[n] = True

    while q:
        x, cnt = q.popleft()
        if x == K:
            return cnt
        for num in [x - 1, x + 1, x * 2]:
            if 0 <= num <= max_cnt and not v[num]:
                v[num] = True
                q.append([num, cnt + 1])


ans = bfs(N)
print(ans)

