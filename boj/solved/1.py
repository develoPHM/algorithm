N = int(input())
paper = []
white = 0
blue = 0
for _ in range(N):
    paper.append(list(map(int, input().split())))


def one(a, n):
    a = [0,0]
    one_paper = []
    for i in range(a[0],n):
        li = []
        for j in range(a[1],n):
            li.append(paper[i][j])
        one_paper.append(li)
    return one_paper