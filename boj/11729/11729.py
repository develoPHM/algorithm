# n - 1 탑을 2번째 위치로 옮김
# n 번째 층을 3번째 위치로 옮김
# 3번째 위치에 다시 n - 1 탑을 쌓음.
def hanoi(n, start, end):
    # 잠시 옮기는 기둥 2로 초기화 하면 재귀에서 문제 발생.
    # start = 1, end = 2 일 때 keep 이 3이 되야 하는데 2임
    keep = 6 - (start + end)
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, keep)
    print(start, end)
    hanoi(n - 1, keep, end)


n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3)
