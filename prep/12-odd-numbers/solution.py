def solution(n):
    odd_numbers = []

    for number in range(1, n + 1):
        if number % 2 == 1:
            odd_numbers.append(number)

    return odd_numbers
