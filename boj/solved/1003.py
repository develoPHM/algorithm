def fibo(n):
    dp_0 = [0] * (n + 1)
    dp_1 = [0] * (n + 1)
    dp_0[0] = 1
    dp_1[1] = 1

    for i in range(2, n + 1):
        dp_0[i] = dp_0[i - 1] + dp_0[i - 2]
        dp_1[i] = dp_1[i - 1] + dp_1[i - 2]
    return dp_0, dp_1

dp_0, dp_1 = fibo(40)

T = int(input())
for _ in range(T):
    num = int(input())
    print(dp_0[num], dp_1[num])
