def solution(arr, divisor):
    divisible = []
    for number in arr:
        if number % divisor == 0:
            divisible.append(number)

    if len(divisible) == 0:
        return [-1]
    return sorted(divisible)
