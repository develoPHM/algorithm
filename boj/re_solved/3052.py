# li = []
# for i in range(10):
#     num = int(input())
#     if num % 42 in li:
#         continue
#     li.append(num % 42)
# print(len(li))
# # O(N제곱)
a = [0] * 42
for i in range(10):
    num = int(input())
    a[num % 42] = 1

print(sum(a))