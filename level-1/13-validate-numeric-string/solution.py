def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False

    for character in s:
        if character not in "0123456789":
            return False
    return True
