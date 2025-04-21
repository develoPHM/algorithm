# N = int(input())
# check = False
# for x in range(10):
#     if check:
#         break
#     for y in range(10):
#         if check:
#             break
#         for z in range(10):
#             if x + y + z + int(str(x)+str(y)+str(z)) == N:
#                 print(int(str(x)+str(y)+str(z)))
#                 check = True
#                 break
# if check == False:
#     print(0)
N = int(input())
check = False
for num in range(1, N + 1):
    sum = 0
    for c in list(str(num)):
        sum += int(c)
    if sum + num == N:
        check = True
        break
if check == False:
    print(0)
else:
    print(num)
