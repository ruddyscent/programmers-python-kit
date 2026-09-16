def solution(numbers):
    sums = set()
    for first in range(len(numbers)):
        for second in range(first + 1, len(numbers)):
            sums.add(numbers[first] + numbers[second])
    return sorted(sums)
