def solution(arr):
    if len(arr) == 1:
        return [-1]

    smallest = min(arr)
    remaining = []
    for number in arr:
        if number != smallest:
            remaining.append(number)
    return remaining
