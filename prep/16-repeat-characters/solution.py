def solution(my_string, n):
    answer = ""

    for character in my_string:
        answer += character * n

    return answer
