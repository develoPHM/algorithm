N = int(input())
num = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
min_num, max_num = int(1e9), int(-1e9)


def dfs(n, sm, plus, minus, multiply, divide):
    global min_num, max_num
    if n == N:  # 종료조건
        min_num = min(min_num, sm)
        max_num = max(max_num, sm)
        return

    if plus > 0:
        dfs(n + 1, sm + num[n], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(n + 1, sm - num[n], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(n + 1, sm * num[n], plus, minus, multiply - 1, divide)
    if divide > 0:
        dfs(n + 1, int(sm / num[n]), plus, minus, multiply, divide - 1)


dfs(1, num[0], plus, minus, multiply, divide)

print(max_num, min_num, sep='\n')
