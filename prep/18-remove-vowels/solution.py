def solution(my_string):
    vowels = "aeiou"
    answer = ""

    for character in my_string:
        if character not in vowels:
            answer += character

    return answer
