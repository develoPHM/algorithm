# def solution(n):
#     cnt = 1
#     if n == 1 or n == 2:
#         return cnt
#
#     for i in range(1, n // 2 + 2):
#         num = 0
#         for j in range(i, n // 2 + 2):
#             if num > n:
#                 break
#             num += j
#             if num == n:
#                 cnt += 1
#                 break
#     return cnt
#
# def solution(n):
#     cnt = 0
#     k = 1  # 연속된 자연수의 개수
#
#     while k * (k - 1) // 2 < n:  # 조건: k * (k - 1) // 2 <= n
#         # n - k * (k - 1) // 2 가 k로 나누어떨어져야 함
#         if (n - k * (k - 1) // 2) % k == 0:
#             cnt += 1
#         k += 1
#
#     return cnt