from collections import deque


def solution(maps):
    rows = len(maps)
    columns = len(maps[0])
    distances = []
    for row in range(rows):
        distances.append([-1] * columns)
    distances[0][0] = 1
    queue = deque([(0, 0)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        row, column = queue.popleft()
        if row == rows - 1 and column == columns - 1:
            return distances[row][column]
        for row_change, column_change in directions:
            next_row = row + row_change
            next_column = column + column_change
            if not (0 <= next_row < rows and 0 <= next_column < columns):
                continue
            if maps[next_row][next_column] == 0:
                continue
            if distances[next_row][next_column] != -1:
                continue
            distances[next_row][next_column] = distances[row][column] + 1
            queue.append((next_row, next_column))
    return -1
