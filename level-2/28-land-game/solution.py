def solution(land):
    previous = land[0][:]
    for row in range(1, len(land)):
        current = [0] * 4
        for column in range(4):
            best_before = 0
            for last_column in range(4):
                if last_column != column:
                    best_before = max(best_before, previous[last_column])
            current[column] = land[row][column] + best_before
        previous = current
    return max(previous)
