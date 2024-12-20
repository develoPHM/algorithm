def solution(lottos, win_nums):
    score = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    zero = 0
    correct = []
    for c in range(lottos.count(0)):
        lottos.remove(0)
        zero += 1

    for c in lottos:
        if c in win_nums:
            correct.append(c)

    return [score[len(correct) + zero], score[len(correct)]]