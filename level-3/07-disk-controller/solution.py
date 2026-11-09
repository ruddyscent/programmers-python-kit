from heapq import heappop, heappush


def solution(jobs):
    tasks = []
    for number in range(len(jobs)):
        request, duration = jobs[number]
        tasks.append((request, duration, number))
    tasks.sort()

    waiting = []
    time = 0
    next_task = 0
    finished = 0
    total_turnaround = 0
    while finished < len(tasks):
        while next_task < len(tasks) and tasks[next_task][0] <= time:
            request, duration, number = tasks[next_task]
            heappush(waiting, (duration, request, number))
            next_task += 1
        if waiting:
            duration, request, number = heappop(waiting)
            time += duration
            total_turnaround += time - request
            finished += 1
        else:
            time = tasks[next_task][0]
    return total_turnaround // len(jobs)
