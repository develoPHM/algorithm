def dfs(n, a_list, b_list):
    global ans
    if n == N:
        if len(a_list) == len(b_list):  # 같은 인원수로 팀을 구성
            a_sum = b_sum = 0
            for i in range(M):
                for j in range(M):
                    a_sum += arr[a_list[i]][a_list[j]]
                    b_sum += arr[b_list[i]][b_list[j]]
            ans = min(ans, abs(a_sum - b_sum))
        return

    dfs(n + 1, a_list + [n], b_list)  # A팀 선택
    dfs(n + 1, a_list, b_list + [n])  # B팀 선택


N = int(input())
M = N // 2  # 팀 인원
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 100 * M * M
dfs(0, [], [])
print(ans)
