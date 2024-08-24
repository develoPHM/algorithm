# n = 선택된 숫자 개수 (길이)
def dfs(n, li):
    if n == M:  # M개의 수열을 완성
        ans.append(li)
        return
    # 하부 단계 호출
    for i in range(1, N + 1):
        if not v[i]:
            v[i] = True
            dfs(n + 1, li + [i])
            v[i] = False


N, M = map(int, input().split())

ans = []  # 정답 리스트를 저장할 리스트
v = [False] * (N + 1)  # 중복확인

dfs(0, []) # 시작
for c in ans:
    print(*c)
b