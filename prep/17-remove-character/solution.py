def solution(my_string, letter):
    answer = ""

    for character in my_string:
        if character != letter:
            answer += character

    return answer
