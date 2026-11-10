from heapq import heappop, heappush


def solution(n, s, a, b, fares):
    roads = []
    for point in range(n + 1):
        roads.append([])
    for first, second, fare in fares:
        roads[first].append((second, fare))
        roads[second].append((first, fare))

    def cheapest_from(start):
        costs = [float("inf")] * (n + 1)
        costs[start] = 0
        heap = [(0, start)]
        while heap:
            cost, point = heappop(heap)
            if cost > costs[point]:
                continue
            for next_point, fare in roads[point]:
                new_cost = cost + fare
                if new_cost < costs[next_point]:
                    costs[next_point] = new_cost
                    heappush(heap, (new_cost, next_point))
        return costs

    from_s = cheapest_from(s)
    from_a = cheapest_from(a)
    from_b = cheapest_from(b)
    best = float("inf")
    for split in range(1, n + 1):
        best = min(best, from_s[split] + from_a[split] + from_b[split])
    return best
