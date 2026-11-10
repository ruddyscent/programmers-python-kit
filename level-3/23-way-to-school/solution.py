def solution(m, n, puddles):
    divisor = 1000000007
    flooded = set()
    for column, row in puddles:
        flooded.add((row, column))

    ways = []
    for row in range(n + 1):
        ways.append([0] * (m + 1))
    ways[1][1] = 1

    for row in range(1, n + 1):
        for column in range(1, m + 1):
            if row == 1 and column == 1:
                continue
            if (row, column) in flooded:
                continue
            ways[row][column] = (ways[row - 1][column] + ways[row][column - 1]) % divisor
    return ways[n][m]
