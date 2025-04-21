N = int(input())
for _ in range(N):
    a = input()


    def pal(a, front, back, cnt, check):
        if front >= back:
            return check, cnt

        if a[front] == a[back]:
            cnt += 1
            return pal(a, front + 1, back - 1, cnt, check)
        else:
            check = 0
            return check, cnt


    print(pal(a, 0, len(a) - 1, 1, 1))
