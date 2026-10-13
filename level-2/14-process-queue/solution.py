from collections import deque


def solution(priorities, location):
    queue = deque()
    for index in range(len(priorities)):
        queue.append((index, priorities[index]))

    executed = 0
    while queue:
        index, priority = queue.popleft()
        has_higher = False
        for waiting in queue:
            if waiting[1] > priority:
                has_higher = True
                break
        if has_higher:
            queue.append((index, priority))
        else:
            executed += 1
            if index == location:
                return executed
