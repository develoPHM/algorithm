A, B = map(int,input().split())
A_dict = {}
B_dict = {}
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
cnt = 0
for c in A_list:
    A_dict[c] = 1
for c in B_list:
    B_dict[c] = 1
# A-B
for c in A_dict:
    if c in B_dict:
        continue
    cnt += 1
# B-A
for c in B_dict:
    if c in A_dict:
        continue
    cnt += 1
print(cnt)