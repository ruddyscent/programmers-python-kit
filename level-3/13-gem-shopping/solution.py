def solution(gems):
    kinds = len(set(gems))
    counts = {}
    best_start = 0
    best_end = len(gems) - 1
    start = 0
    for end in range(len(gems)):
        gem = gems[end]
        counts[gem] = counts.get(gem, 0) + 1
        while len(counts) == kinds:
            if end - start < best_end - best_start:
                best_start = start
                best_end = end
            start_gem = gems[start]
            counts[start_gem] -= 1
            if counts[start_gem] == 0:
                del counts[start_gem]
            start += 1
    return [best_start + 1, best_end + 1]
