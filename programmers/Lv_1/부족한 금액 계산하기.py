def solution(price, money, count):
    ans = 0
    for i in range(1, count + 1):
        cost = price * i
        ans += cost

    if money >= ans:
        return 0
    else:
        return ans - money