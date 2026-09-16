def solution(d, budget):
    requests = sorted(d)
    spent = 0
    supported = 0
    for amount in requests:
        if spent + amount > budget:
            break
        spent += amount
        supported += 1
    return supported
