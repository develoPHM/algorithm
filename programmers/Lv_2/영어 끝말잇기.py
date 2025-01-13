def solution(n, words):
    li = []
    people = 1
    turn = 1
    ans = [0, 0]

    for c in words:
        if people == n + 1:
            people = 1
            turn += 1

        if c in li:
            ans = [people, turn]
            break

        elif len(li) > 0 and li[-1][-1] != c[0]:
            ans = [people, turn]
            break
        else:
            people += 1
            li.append(c)

    return ans