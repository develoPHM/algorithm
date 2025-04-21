N, K = map(int, input().split())
ondo = list(map(int, input().split()))

save = [sum(ondo[0:K])]
for i in range(N - K):
    save.append(save[i] - ondo[i] + ondo[K + i])
print(max(save))