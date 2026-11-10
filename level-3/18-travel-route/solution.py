import sys


def solution(tickets):
    sys.setrecursionlimit(20000)
    routes = {}
    for index in range(len(tickets)):
        start, end = tickets[index]
        if start not in routes:
            routes[start] = []
        routes[start].append((end, index))
    for start in routes:
        routes[start].sort()

    used = [False] * len(tickets)
    path = ["ICN"]

    def travel(airport):
        if len(path) == len(tickets) + 1:
            return True
        for end, index in routes.get(airport, []):
            if used[index]:
                continue
            used[index] = True
            path.append(end)
            if travel(end):
                return True
            used[index] = False
            path.pop()
        return False

    travel("ICN")
    return path
