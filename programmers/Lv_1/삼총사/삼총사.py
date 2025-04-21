number = [-3, -2, -1, 0, 1, 2, 3]
number.sort()
cnt = 0
for i in range(len(number)):
    for j in range(i + 1, len(number)):
        for k in range(j + 1, len(number)):
            if number[i] + number[j] + number[k] == 0:
                cnt += 1