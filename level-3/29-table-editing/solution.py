def solution(n, k, cmd):
    above = []
    below = []
    for row in range(n):
        above.append(row - 1)
        below.append(row + 1)
    below[n - 1] = -1

    deleted = [False] * n
    removed = []
    current = k
    for command in cmd:
        parts = command.split()
        if parts[0] == "U":
            for step in range(int(parts[1])):
                current = above[current]
        elif parts[0] == "D":
            for step in range(int(parts[1])):
                current = below[current]
        elif parts[0] == "C":
            deleted[current] = True
            removed.append(current)
            up = above[current]
            down = below[current]
            if up != -1:
                below[up] = down
            if down != -1:
                above[down] = up
            if down != -1:
                current = down
            else:
                current = up
        else:
            row = removed.pop()
            deleted[row] = False
            up = above[row]
            down = below[row]
            if up != -1:
                below[up] = row
            if down != -1:
                above[down] = row

    marks = []
    for row in range(n):
        if deleted[row]:
            marks.append("X")
        else:
            marks.append("O")
    return "".join(marks)
