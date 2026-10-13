def solution(s):
    converted = []
    for word in s.split(" "):
        converted.append(word.capitalize())
    return " ".join(converted)
