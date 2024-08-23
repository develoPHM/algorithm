def dfs(n, lst):
    if n == M:  # M개의 수열을 완성
        ans.append(lst)
        return
    # 하부 단계 호출
    for j in range(1, N + 1):
        if v[j] == 0:
            v[j] = 1
            dfs(n + 1, lst + [j])
            v[j] = 0


N, M = map(int, input().split())

ans = []  # 정답 리스트를 저장할 리스트
v = [0] * (N + 1)  # 중복확인

dfs(0, [])
for c in ans:
    print(*c)
