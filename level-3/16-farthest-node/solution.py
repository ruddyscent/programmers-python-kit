from collections import deque


def solution(n, edge):
    neighbors = []
    for node in range(n + 1):
        neighbors.append([])
    for first, second in edge:
        neighbors[first].append(second)
        neighbors[second].append(first)

    distances = [-1] * (n + 1)
    distances[1] = 0
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor in neighbors[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    farthest = max(distances)
    return distances.count(farthest)
