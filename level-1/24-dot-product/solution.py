def solution(a, b):
    total = 0
    for index in range(len(a)):
        total += a[index] * b[index]
    return total
