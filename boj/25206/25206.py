sum = 0
sum_score = 0
for _ in range(20):
    result = input()
    if result[-1:] == 'P':
        continue
    elif result[-1:] == 'F':
        score = int(result[-5:-4]) * 0.0
        sum += score
        sum_score += int(result[-5:-4])
    elif result[-2:] == 'A+':
        score = int(result[-6:-5]) * 4.5
        sum += score
        sum_score += int(result[-6:-5])
    elif result[-2:] == 'A0':
        score = int(result[-6:-5]) * 4.0
        sum += score
        sum_score += int(result[-6:-5])
    elif result[-2:] == 'B+':
        score = int(result[-6:-5]) * 3.5
        sum += score
        sum_score += int(result[-6:-5])
    elif result[-2:] == 'B0':
        score = int(result[-6:-5]) * 3.0
        sum += score
        sum_score += int(result[-6:-5])
    elif result[-2:] == 'C+':
        score = int(result[-6:-5]) * 2.5
        sum += score
        sum_score += int(result[-6:-5])
    elif result[-2:] == 'C0':
        score = int(result[-6:-5]) * 2.0
        sum += score
        sum_score += int(result[-6:-5])
    elif result[-2:] == 'D+':
        score = int(result[-6:-5]) * 1.5
        sum += score
        sum_score += int(result[-6:-5])
    elif result[-2:] == 'D0':
        score = int(result[-6:-5]) * 1.0
        sum += score
        sum_score += int(result[-6:-5])
print(sum / sum_score)
