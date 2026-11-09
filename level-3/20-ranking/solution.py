def solution(n, results):
    wins = []
    for player in range(n + 1):
        wins.append([False] * (n + 1))
    for winner, loser in results:
        wins[winner][loser] = True

    for middle in range(1, n + 1):
        for winner in range(1, n + 1):
            if not wins[winner][middle]:
                continue
            for loser in range(1, n + 1):
                if wins[middle][loser]:
                    wins[winner][loser] = True

    ranked = 0
    for player in range(1, n + 1):
        known = 0
        for other in range(1, n + 1):
            if wins[player][other] or wins[other][player]:
                known += 1
        if known == n - 1:
            ranked += 1
    return ranked
