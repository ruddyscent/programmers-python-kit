from math import gcd


def solution(arr):
    multiple = 1
    for number in arr:
        multiple = multiple // gcd(multiple, number) * number
    return multiple
