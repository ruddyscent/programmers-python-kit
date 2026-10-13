def solution(n):
    left = 1
    total = 0
    count = 0
    for right in range(1, n + 1):
        total += right
        while total > n:
            total -= left
            left += 1
        if total == n:
            count += 1
    return count
