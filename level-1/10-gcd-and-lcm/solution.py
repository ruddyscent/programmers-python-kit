def solution(n, m):
    greatest_divisor = 1
    for divisor in range(1, min(n, m) + 1):
        if n % divisor == 0 and m % divisor == 0:
            greatest_divisor = divisor

    least_multiple = n * m // greatest_divisor
    return [greatest_divisor, least_multiple]
