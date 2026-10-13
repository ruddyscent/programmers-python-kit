from itertools import permutations
from math import isqrt


def solution(numbers):
    candidates = set()
    for length in range(1, len(numbers) + 1):
        for digits in permutations(numbers, length):
            candidates.add(int("".join(digits)))

    count = 0
    for candidate in candidates:
        if candidate < 2:
            continue
        is_prime = True
        for divisor in range(2, isqrt(candidate) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count
