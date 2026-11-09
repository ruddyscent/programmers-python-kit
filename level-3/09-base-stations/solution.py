def solution(n, stations, w):
    coverage = 2 * w + 1
    added = 0
    first_uncovered = 1
    for station in stations:
        left = station - w
        if first_uncovered < left:
            gap = left - first_uncovered
            added += (gap + coverage - 1) // coverage
        first_uncovered = station + w + 1

    if first_uncovered <= n:
        gap = n - first_uncovered + 1
        added += (gap + coverage - 1) // coverage
    return added
