def solution(n):
    for divisor in range(2, n):
        if n % divisor == 1:
            return divisor
