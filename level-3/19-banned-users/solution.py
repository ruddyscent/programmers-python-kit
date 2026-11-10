def solution(user_id, banned_id):
    def matches(user, pattern):
        if len(user) != len(pattern):
            return False
        for index in range(len(user)):
            if pattern[index] != "*" and pattern[index] != user[index]:
                return False
        return True

    candidates = []
    for pattern in banned_id:
        matched = []
        for user_index in range(len(user_id)):
            if matches(user_id[user_index], pattern):
                matched.append(user_index)
        candidates.append(matched)

    found_sets = set()
    chosen = []

    def choose(position):
        if position == len(candidates):
            found_sets.add(tuple(sorted(chosen)))
            return
        for user_index in candidates[position]:
            if user_index in chosen:
                continue
            chosen.append(user_index)
            choose(position + 1)
            chosen.pop()

    choose(0)
    return len(found_sets)
