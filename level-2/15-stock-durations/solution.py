def solution(prices):
    durations = [0] * len(prices)
    waiting = []
    for current in range(len(prices)):
        while waiting and prices[waiting[-1]] > prices[current]:
            previous = waiting.pop()
            durations[previous] = current - previous
        waiting.append(current)

    last = len(prices) - 1
    for previous in waiting:
        durations[previous] = last - previous
    return durations
