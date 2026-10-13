def solution(people, limit):
    weights = sorted(people)
    light = 0
    heavy = len(weights) - 1
    boats = 0
    while light <= heavy:
        if light < heavy and weights[light] + weights[heavy] <= limit:
            light += 1
        heavy -= 1
        boats += 1
    return boats
