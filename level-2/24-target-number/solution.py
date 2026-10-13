def solution(numbers, target):
    def search(index, total):
        if index == len(numbers):
            if total == target:
                return 1
            return 0
        added = search(index + 1, total + numbers[index])
        subtracted = search(index + 1, total - numbers[index])
        return added + subtracted

    return search(0, 0)
