progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
ans = []
while len(progresses) > 0:
    for i in range(len(progresses)):
        progresses[i] += speeds[i]
        if progresses[i] > 100:
            progresses[i] = 100

    cnt = 0
    for c in progresses:
        if c != 100:
            break
        elif c == 100:
            cnt += 1

    if cnt > 0:
        ans.append(cnt)

    for i in range(cnt):
        progresses.pop(0)
        speeds.pop(0)

print(ans)