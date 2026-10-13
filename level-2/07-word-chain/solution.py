def solution(n, words):
    seen = set()
    for index in range(len(words)):
        word = words[index]
        if word in seen:
            return [index % n + 1, index // n + 1]
        if index > 0 and words[index - 1][-1] != word[0]:
            return [index % n + 1, index // n + 1]
        seen.add(word)
    return [0, 0]
