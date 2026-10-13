def solution(clothes):
    category_counts = {}
    for name, category in clothes:
        category_counts[category] = category_counts.get(category, 0) + 1

    combinations = 1
    for count in category_counts.values():
        combinations *= count + 1
    return combinations - 1
