def solution(s):
    dic = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    check = ''
    result = ''
    for c in s:
        if check in dic:
            result += dic[check]
            check = ''
        if c.isdigit():
            result += c
        else:
            check += c
    if len(check) > 0:
        result += dic[check]
    return int(result)