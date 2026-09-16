def solution(strings, n):
    def sort_key(word):
        return (word[n], word)

    return sorted(strings, key=sort_key)
