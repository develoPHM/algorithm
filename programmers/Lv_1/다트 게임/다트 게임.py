def solution(dartResult):
    score = [0, 0, 0, 0]
    now = 1
    num = 0
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            score[now] += int(dartResult[num: i])
            now += 1
            num = i + 1
        elif dartResult[i] == 'D':
            score[now] += int(dartResult[num: i]) ** 2
            now += 1
            num = i + 1
        elif dartResult[i] == 'T':
            score[now] += int(dartResult[num: i]) ** 3
            print(dartResult[num: i])
            now += 1
            num = i + 1
        if dartResult[i] == '*':
            score[now - 2] *= 2
            score[now - 1] *= 2
            num = i + 1
        elif dartResult[i] == '#':
            score[now - 1] *= -1
            num = i + 1
    return sum(score)