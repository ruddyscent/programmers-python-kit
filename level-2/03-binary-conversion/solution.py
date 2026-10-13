def solution(s):
    conversions = 0
    removed_zeros = 0
    while s != "1":
        ones = s.count("1")
        removed_zeros += len(s) - ones
        s = bin(ones)[2:]
        conversions += 1
    return [conversions, removed_zeros]
