S = input()
S_set = set()
for i in range(1, len(S) + 1):
    for j in range(len(S)):
        if j + i <= len(S):
            S_set.add(S[j:j + i])
print(len(S_set))