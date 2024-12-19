N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
stage_cnt = [0] * (N + 2)  # 스테이지는 1~N, N+1은 클리어한 사용자
people = len(stages)

for stage in stages:
    stage_cnt[stage] += 1
# 실패율 계산
arr = []
for i in range(1, N + 1):
    if people > 0:
        rate = stage_cnt[i] / people
        people -= stage_cnt[i]
    else:
        rate = 0
    arr.append((i, rate))
arr.sort(key=lambda x:x[1], reverse=True)
ans = []
for c in arr:
    ans.append(c[0])
print(ans)