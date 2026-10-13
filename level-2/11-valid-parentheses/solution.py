def solution(s):
    unclosed = 0
    for character in s:
        if character == "(":
            unclosed += 1
        else:
            unclosed -= 1
        if unclosed < 0:
            return False
    return unclosed == 0
