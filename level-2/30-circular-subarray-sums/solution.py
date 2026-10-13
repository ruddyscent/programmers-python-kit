def solution(elements):
    size = len(elements)
    doubled = elements + elements
    prefix = [0]
    for number in doubled:
        prefix.append(prefix[-1] + number)

    sums = set()
    for start in range(size):
        for length in range(1, size + 1):
            total = prefix[start + length] - prefix[start]
            sums.add(total)
    return len(sums)
