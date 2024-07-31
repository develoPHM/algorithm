import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):

    num = int(input())
    while True:
        check = True
        if num in [0, 1, 2]:
            print(2)
            break

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                check = False
                break

        if check:
            print(num)
            break
        else:
            num += 1
