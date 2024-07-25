li = []
for i in range(9): 
    li.append(int(input()))
m = 0
j = 0
for i in range(9):
    if li[i] > m:
        m = li[i]
        j = i + 1
print(m)
print(j)
# O(N)