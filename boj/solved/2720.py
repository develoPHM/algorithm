T = int(input())
# T = 124
Q, D, N, P = 25, 10, 5, 1

for _ in range(T):
    ans = []
    cost = int(input())
    ans.append(cost // Q)
    cost = cost % Q
    ans.append(cost // D)
    cost = cost % D
    ans.append(cost // N)
    cost = cost % N
    ans.append(cost // P)
    cost = cost % P
    print(*ans)