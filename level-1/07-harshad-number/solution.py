def solution(x):
    digit_sum = 0
    for character in str(x):
        digit_sum += int(character)
    return x % digit_sum == 0
