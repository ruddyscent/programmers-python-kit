def solution(n):
    total = 0
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            total += divisor
    return total
