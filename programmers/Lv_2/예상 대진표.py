def solution(n,a,b):
    li = [0] * n
    li[a - 1], li[b - 1] = 1, 1
    cnt = 0
    check = 1

    while check:
        match = []
        for i in range(0, len(li), 2):
            if li[i] == 1 and li[i + 1] == 1:
                check = 0
            if li[i] == 1 or li[i + 1] == 1:
                match.append(1)
            else:
                match.append(li[i])
        cnt += 1
        li = match
    return cnt

# --------------- #
def solution(n, A, B):
    cnt = 0
    while A != B:
        # 다음 라운드 번호는 (현재번호 + 1) // 2
        A = (A + 1) // 2
        B = (B + 1) // 2
        cnt += 1
    return cnt