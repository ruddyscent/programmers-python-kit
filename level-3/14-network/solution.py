def solution(n, computers):
    visited = [False] * n
    networks = 0
    for start in range(n):
        if visited[start]:
            continue
        networks += 1
        visited[start] = True
        stack = [start]
        while stack:
            computer = stack.pop()
            for neighbor in range(n):
                if computers[computer][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
    return networks
