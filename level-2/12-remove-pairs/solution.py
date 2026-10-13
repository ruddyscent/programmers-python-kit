def solution(s):
    stack = []
    for character in s:
        if stack and stack[-1] == character:
            stack.pop()
        else:
            stack.append(character)
    if len(stack) == 0:
        return 1
    return 0
