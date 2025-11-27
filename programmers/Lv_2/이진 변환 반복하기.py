def solution(s):
    delete_zero = 0
    cnt = 0
    while len(s) > 1:
        cnt += 1
        no_zero = ''
        for c in s:
            if c == '0':
                delete_zero += 1
                continue
            else:
                no_zero += c
        new_zero = len(no_zero) # 0 뺸 수의 길이
        new_2 = ''

        print('0뺸수', new_zero)
        while new_zero > 1:
            plus = new_zero % 2
            new_2 += str(plus)
            new_zero = new_zero // 2
        new_2 += str(new_zero)

        s = new_2[::-1]
    return [cnt, delete_zero]

