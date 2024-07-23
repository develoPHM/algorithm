N = int(input())

for _ in range(N):
    OX = input()
    sum = 0
    score = 0
    for i in range(len(OX)):
        if OX[i] == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)