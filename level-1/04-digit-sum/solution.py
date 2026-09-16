def solution(n):
    total = 0
    for character in str(n):
        total += int(character)
    return total
