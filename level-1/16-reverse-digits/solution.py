def solution(n):
    digits = []
    for character in str(n)[::-1]:
        digits.append(int(character))
    return digits
