def solution(progresses, speeds):
    batches = []
    release_day = 0
    for index in range(len(progresses)):
        remaining = 100 - progresses[index]
        speed = speeds[index]
        days = (remaining + speed - 1) // speed
        if days > release_day:
            release_day = days
            batches.append(1)
        else:
            batches[-1] += 1
    return batches
