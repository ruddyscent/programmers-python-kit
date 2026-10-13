from heapq import heapify, heappop, heappush


def solution(scoville, K):
    foods = scoville[:]
    heapify(foods)
    mixed = 0
    while foods[0] < K:
        if len(foods) < 2:
            return -1
        first = heappop(foods)
        second = heappop(foods)
        heappush(foods, first + 2 * second)
        mixed += 1
    return mixed
