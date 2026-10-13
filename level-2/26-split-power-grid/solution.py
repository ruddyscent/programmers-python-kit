from collections import deque


def solution(n, wires):
    neighbors = []
    for node in range(n + 1):
        neighbors.append([])
    for first, second in wires:
        neighbors[first].append(second)
        neighbors[second].append(first)

    best = n
    for cut_first, cut_second in wires:
        visited = [False] * (n + 1)
        visited[cut_first] = True
        queue = deque([cut_first])
        connected = 0
        while queue:
            node = queue.popleft()
            connected += 1
            for neighbor in neighbors[node]:
                is_cut = (node == cut_first and neighbor == cut_second)
                is_cut = is_cut or (node == cut_second and neighbor == cut_first)
                if is_cut or visited[neighbor]:
                    continue
                visited[neighbor] = True
                queue.append(neighbor)
        best = min(best, abs(n - 2 * connected))
    return best
