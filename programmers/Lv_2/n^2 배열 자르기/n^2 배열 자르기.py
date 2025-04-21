def solution(n, left, right):
    ans = []
    for i in range(left, right + 1):
        a = i // n  # 몫
        b = i % n  # 나머지
        if a < b:
            a, b = b, a
        ans.append(a + 1)

    return ans