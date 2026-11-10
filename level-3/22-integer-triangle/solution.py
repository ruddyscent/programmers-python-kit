def solution(triangle):
    best = [triangle[0][0]]
    for row in range(1, len(triangle)):
        current = []
        for column in range(row + 1):
            if column == 0:
                from_above = best[0]
            elif column == row:
                from_above = best[column - 1]
            else:
                from_above = max(best[column - 1], best[column])
            current.append(from_above + triangle[row][column])
        best = current
    return max(best)
