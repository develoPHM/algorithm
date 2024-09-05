N = int(input())
people = list(map(int,input().split()))
people.sort()
time = 0
ans =[0] * N
for i in range(N):
    time = time + people[i]
    ans[i] = time
print(sum(ans))