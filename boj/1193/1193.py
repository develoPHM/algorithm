# X = int(input())
# a, b = 0, 0
# cnt = 1
# step = 2
# if X == 1:
#     print(1, '/', 1, sep='')
# else:
#     while cnt != X:
#         if step % 2 == 0:  # 짝수면
#             for i in range(0, step):
#                 cnt += 1
#                 a = i + 1
#                 b = step - i
#                 # print(cnt,'cnt :',a,b)
#                 if cnt == X:
#                     break
#         else:  # 홀수면
#             for i in range(0, step):
#                 cnt += 1
#                 b = i + 1
#                 a = step - i
#                 # print(cnt,'cnt :',a,b)
#                 if cnt == X:
#                     break
#         step += 1
#     print(a, '/', b, sep='')
X = int(input())
total = 0
n = 1
while (total + n) < X:
    total += n
    n += 1

if n % 2 == 0:
    a, b = X - total , n - (X - total - 1)
else:
    a, b = n - (X - total - 1), X - total
print(a,'/',b, sep='')

# print('n:', n, 'total:', total)