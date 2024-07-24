N = int(input())

for _ in range(N):
    OX = input()
    sum = 0
    score = 0
    for i in range(len(OX)):
        if OX[i] == 'X':
            score = 0
            continue
        score += 1
        sum += score
    print(sum)