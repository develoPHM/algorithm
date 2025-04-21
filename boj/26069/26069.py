N = int(input())
li = {"ChongChong"}

for _ in range(N):
    A, B = input().split()
    if A in li:
        li.add(B)
    if B in li:
        li.add(A)
print(len(li))