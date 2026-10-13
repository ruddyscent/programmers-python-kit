def solution(s):
    numbers = []
    for token in s.split():
        numbers.append(int(token))
    return str(min(numbers)) + " " + str(max(numbers))
