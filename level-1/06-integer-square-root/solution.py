from math import isqrt


def solution(n):
    root = isqrt(n)
    if root * root == n:
        return (root + 1) * (root + 1)
    return -1
