def solution(num):
    cnt = 0
    ans = 0
    while num > 1:
        cnt += 1
        if num == 1 or cnt == 500:
            break
        if num % 2 == 0:
            num = num // 2
            ans += 1
        elif num % 2 == 1:
            num = num * 3 + 1
            ans += 1
    if cnt == 500:
        return -1
    else:
        return ans