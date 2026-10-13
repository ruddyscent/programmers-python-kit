from functools import cmp_to_key


def solution(numbers):
    parts = []
    for number in numbers:
        parts.append(str(number))

    def compare(first, second):
        if first + second > second + first:
            return -1
        if first + second < second + first:
            return 1
        return 0

    parts.sort(key=cmp_to_key(compare))
    if parts[0] == "0":
        return "0"
    return "".join(parts)
