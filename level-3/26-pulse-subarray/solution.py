def solution(sequence):
    best = sequence[0]
    for first_sign in [1, -1]:
        sign = first_sign
        ending_here = 0
        for value in sequence:
            pulsed = value * sign
            ending_here = max(pulsed, ending_here + pulsed)
            best = max(best, ending_here)
            sign = -sign
    return best
