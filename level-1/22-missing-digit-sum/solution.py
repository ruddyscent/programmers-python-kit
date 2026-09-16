def solution(numbers):
    total = 0
    for digit in range(10):
        if digit not in numbers:
            total += digit
    return total
