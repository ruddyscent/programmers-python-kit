def solution(s):
    middle = len(s) // 2
    if len(s) % 2 == 1:
        return s[middle]
    return s[middle - 1:middle + 1]
