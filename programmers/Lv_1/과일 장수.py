def solution(k, m, score):
    score.sort(reverse=True)
    ans = 0

    if len(score) < m:
        return 0
    else:
        for i in range(0,len(score), m):
            if len(score[i:i+m]) == m:
                ans += min(score[i:i+m]) * m
    return ans