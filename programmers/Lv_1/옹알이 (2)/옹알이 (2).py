def solution(babbling):
    baby = ['aya', 'ye', 'woo', 'ma']
    cnt = 0
    for talk in babbling:
        for c in baby:
            if c * 2 not in talk:
                talk = talk.replace(c, ' ')
        if talk.isspace():
            cnt += 1
    return cnt