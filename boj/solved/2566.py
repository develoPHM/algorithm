cal = []
max_num = 0
x = 0
y = 0
for i in range(9):
    cal.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if cal[i][j] >= max_num:
            max_num = cal[i][j]
            x = i + 1
            y = j + 1
print(max_num)
print(x,y)
