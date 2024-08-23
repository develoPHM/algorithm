def hanoi(num, start, end):
    keep = 6 - (start + end)
    if num == 1:
        li.append([start, end])
        return

    hanoi(num - 1, start, keep)
    li.append([start, end])
    hanoi(num - 1, keep, end)


N = int(input())
li = []
hanoi(N, 1, 3)
print(len(li))
for i in range(len(li)):
    print(li[i][0], li[i][1])
