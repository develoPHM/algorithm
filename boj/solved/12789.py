# from collections import deque
#
# N = int(input())
# li = deque(map(int, input().split())) # 무질서 줄
# go_out = [] # 밥먹으러 가
# wait = [] # 기다려
# num = 1 # 받는 순서
# while len(li) > 0:
#     if li[0] == num:
#         go_out.append(li.popleft())
#         num += 1
#         continue
#     if wait and wait[-1] == num:
#         go_out.append(wait.pop())
#         num += 1
#         continue
#     wait.append(li.popleft())
# go_out = go_out + wait[::-1]
#
# check = []
# for i in range(1, N + 1):
#     check.append(i)
#
# if check == go_out:
#     print('Nice')
# else:
#     print('Sad')