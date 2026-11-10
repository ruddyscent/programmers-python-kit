from heapq import heapify, heappop, heappush


def solution(n, works):
    remaining = []
    for work in works:
        remaining.append(-work)
    heapify(remaining)

    for hour in range(n):
        largest = -heappop(remaining)
        if largest == 0:
            return 0
        heappush(remaining, -(largest - 1))

    fatigue = 0
    for value in remaining:
        fatigue += value * value
    return fatigue
