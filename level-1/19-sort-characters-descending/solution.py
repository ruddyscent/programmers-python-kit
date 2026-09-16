def solution(s):
    characters = sorted(s, reverse=True)
    return "".join(characters)
