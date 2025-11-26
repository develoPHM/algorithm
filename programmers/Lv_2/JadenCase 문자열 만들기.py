def solution(s):
    s = s.lower()
    result = ""
    first = True

    for c in s:
        if first:
            if c.isalpha():
                result += c.upper()
            else:
                result += c
        else:
            result += c

        # 공백이면 다음 글자는 단어 첫 글자
        if c == ' ':
            first = True
        else:
            first = False

    return result
