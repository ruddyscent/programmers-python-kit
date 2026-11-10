from collections import deque


def solution(begin, target, words):
    def one_letter_apart(first, second):
        differences = 0
        for index in range(len(first)):
            if first[index] != second[index]:
                differences += 1
        return differences == 1

    if target not in words:
        return 0
    visited = set()
    queue = deque([(begin, 0)])
    while queue:
        word, steps = queue.popleft()
        if word == target:
            return steps
        for next_word in words:
            if next_word in visited:
                continue
            if one_letter_apart(word, next_word):
                visited.add(next_word)
                queue.append((next_word, steps + 1))
    return 0
