def solution(absolutes, signs):
    total = 0
    for index in range(len(absolutes)):
        if signs[index]:
            total += absolutes[index]
        else:
            total -= absolutes[index]
    return total
