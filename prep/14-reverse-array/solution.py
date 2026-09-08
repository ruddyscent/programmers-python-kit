def solution(num_list):
    reversed_list = []

    for index in range(len(num_list) - 1, -1, -1):
        reversed_list.append(num_list[index])

    return reversed_list
