def solution(word):
    dictionary = []

    def build(prefix):
        if prefix:
            dictionary.append(prefix)
        if len(prefix) == 5:
            return
        for vowel in "AEIOU":
            build(prefix + vowel)

    build("")
    return dictionary.index(word) + 1
