people = [0] * 31 # 학생 수 만큼 길이 초기화
for _ in range(28): # 인풋 받은 학생의 번호를 people의 인덱스에 맞춰 체크
    people[int(input())] += 1
# people 돌면서 체크 안 된 번호 출력
for i in range(1, len(people)):
    if people[i] == 0:
        print(i)
# O(N)