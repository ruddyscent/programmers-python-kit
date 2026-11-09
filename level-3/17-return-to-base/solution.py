from collections import deque


def solution(n, roads, sources, destination):
    neighbors = []
    for area in range(n + 1):
        neighbors.append([])
    for first, second in roads:
        neighbors[first].append(second)
        neighbors[second].append(first)

    distances = [-1] * (n + 1)
    distances[destination] = 0
    queue = deque([destination])
    while queue:
        area = queue.popleft()
        for neighbor in neighbors[area]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[area] + 1
                queue.append(neighbor)

    answer = []
    for source in sources:
        answer.append(distances[source])
    return answer
