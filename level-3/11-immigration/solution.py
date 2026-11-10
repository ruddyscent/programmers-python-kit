def solution(n, times):
    low = 1
    high = min(times) * n
    while low < high:
        middle = (low + high) // 2
        people = 0
        for time in times:
            people += middle // time
        if people >= n:
            high = middle
        else:
            low = middle + 1
    return low
