def solution(s):
    groups = []
    for chunk in s[2:-2].split("},{"):
        group = []
        for token in chunk.split(","):
            group.append(int(token))
        groups.append(group)

    seen = set()
    result = []
    for group in sorted(groups, key=len):
        for number in group:
            if number not in seen:
                seen.add(number)
                result.append(number)
    return result
