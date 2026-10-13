def solution(n):
    two_before = 1
    one_before = 1
    for distance in range(2, n + 1):
        current = (two_before + one_before) % 1234567
        two_before = one_before
        one_before = current
    return one_before
