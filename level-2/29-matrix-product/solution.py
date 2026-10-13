def solution(arr1, arr2):
    rows = len(arr1)
    shared = len(arr2)
    columns = len(arr2[0])
    result = []
    for row in range(rows):
        result_row = []
        for column in range(columns):
            total = 0
            for index in range(shared):
                total += arr1[row][index] * arr2[index][column]
            result_row.append(total)
        result.append(result_row)
    return result
