from itertools import permutations


def solution(k, dungeons):
    best = 0
    for order in permutations(range(len(dungeons))):
        fatigue = k
        explored = 0
        for index in order:
            required, consumed = dungeons[index]
            if fatigue < required:
                break
            fatigue -= consumed
            explored += 1
        best = max(best, explored)
    return best
