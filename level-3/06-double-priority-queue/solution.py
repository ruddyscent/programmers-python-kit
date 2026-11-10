from heapq import heappop, heappush


def solution(operations):
    min_heap = []
    max_heap = []
    counts = {}
    size = 0

    def clean(heap, sign):
        while heap and counts.get(sign * heap[0], 0) == 0:
            heappop(heap)

    for operation in operations:
        command, value_text = operation.split()
        value = int(value_text)
        if command == "I":
            heappush(min_heap, value)
            heappush(max_heap, -value)
            counts[value] = counts.get(value, 0) + 1
            size += 1
        elif size > 0:
            if value == 1:
                clean(max_heap, -1)
                removed = -heappop(max_heap)
            else:
                clean(min_heap, 1)
                removed = heappop(min_heap)
            counts[removed] -= 1
            size -= 1

    if size == 0:
        return [0, 0]
    clean(max_heap, -1)
    clean(min_heap, 1)
    return [-max_heap[0], min_heap[0]]
