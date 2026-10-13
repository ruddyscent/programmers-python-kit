def solution(n):
    required_ones = bin(n).count("1")
    candidate = n + 1
    while bin(candidate).count("1") != required_ones:
        candidate += 1
    return candidate
