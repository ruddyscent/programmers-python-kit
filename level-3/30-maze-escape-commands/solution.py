def solution(n, m, x, y, r, c, k):
    distance = abs(x - r) + abs(y - c)
    if distance > k or (k - distance) % 2 == 1:
        return "impossible"

    moves = [("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0)]
    path = []
    row = x
    column = y
    for step in range(k):
        remaining = k - step - 1
        for letter, row_change, column_change in moves:
            next_row = row + row_change
            next_column = column + column_change
            if not (1 <= next_row <= n and 1 <= next_column <= m):
                continue
            if abs(next_row - r) + abs(next_column - c) <= remaining:
                path.append(letter)
                row = next_row
                column = next_column
                break
    return "".join(path)
