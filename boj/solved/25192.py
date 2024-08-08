N = int(input())
li = []
for _ in range(N):
    li.append(input())
# li = ['ENTER', 'pjshwa', 'chansol', 'chogahui05', 'ENTER', 'pjshwa', 'chansol']
li = ','.join(li).split('ENTER')
people = []
dic = {}
cnt = 0

for i in range(1, len(li)):
    people.append(li[i][1:].split(','))

for i in range(len(people)):
    dic = {}
    for j in range(len(people[i])):
        if people[i][j] == '':
            continue
        if people[i][j] in dic:
            continue

        dic[people[i][j]] = 1
        cnt += 1
print(cnt)