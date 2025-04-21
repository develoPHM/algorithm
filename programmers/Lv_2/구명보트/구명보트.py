def solution(people, limit) :
    cnt = 0
    people.sort()

    l = 0
    r = len(people) - 1
    while l < r :
        if people[r] + people[l] <= limit :
            l += 1
            cnt += 1
        r -= 1
    return len(people) - cnt