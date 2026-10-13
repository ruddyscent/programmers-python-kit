def solution(citations):
    ordered = sorted(citations, reverse=True)
    best = 0
    for index in range(len(ordered)):
        count = index + 1
        if ordered[index] >= count:
            best = count
        else:
            break
    return best
