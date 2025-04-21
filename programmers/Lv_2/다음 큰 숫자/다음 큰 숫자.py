def solution(n):
    cnt_one = bin(n)[2:].count('1')
    ans = 0
    while True:
        n += 1
        check = bin(n)[2:].count('1')
        if cnt_one == check:
            ans = n
            break
    return ans