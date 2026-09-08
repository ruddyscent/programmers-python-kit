def solution(my_string):
    answer = ""
    index = len(my_string) - 1

    while index >= 0:
        answer += my_string[index]
        index -= 1

    return answer
