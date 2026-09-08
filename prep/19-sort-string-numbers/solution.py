def solution(my_string):
    numbers = []

    for character in my_string:
        if character.isdigit():
            numbers.append(int(character))

    return sorted(numbers)
