def solution(sticker):
    def best_in_line(values):
        before_previous = 0
        previous = 0
        for value in values:
            current = max(previous, before_previous + value)
            before_previous = previous
            previous = current
        return previous

    if len(sticker) == 1:
        return sticker[0]
    without_last = best_in_line(sticker[:-1])
    without_first = best_in_line(sticker[1:])
    return max(without_last, without_first)
