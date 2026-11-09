def solution(board, skill):
    rows = len(board)
    columns = len(board[0])
    changes = []
    for row in range(rows + 1):
        changes.append([0] * (columns + 1))

    for kind, r1, c1, r2, c2, degree in skill:
        if kind == 1:
            amount = -degree
        else:
            amount = degree
        changes[r1][c1] += amount
        changes[r1][c2 + 1] -= amount
        changes[r2 + 1][c1] -= amount
        changes[r2 + 1][c2 + 1] += amount

    for row in range(rows + 1):
        for column in range(1, columns + 1):
            changes[row][column] += changes[row][column - 1]
    for row in range(1, rows + 1):
        for column in range(columns + 1):
            changes[row][column] += changes[row - 1][column]

    standing = 0
    for row in range(rows):
        for column in range(columns):
            if board[row][column] + changes[row][column] > 0:
                standing += 1
    return standing
