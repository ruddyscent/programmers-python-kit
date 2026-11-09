def solution(n, s):
    if n > s:
        return [-1]
    base = s // n
    extra = s % n
    return [base] * (n - extra) + [base + 1] * extra
