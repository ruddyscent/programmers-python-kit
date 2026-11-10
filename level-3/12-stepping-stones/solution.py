def solution(stones, k):
    def can_cross(friends):
        sunken_in_row = 0
        for stone in stones:
            if stone < friends:
                sunken_in_row += 1
                if sunken_in_row == k:
                    return False
            else:
                sunken_in_row = 0
        return True

    low = 1
    high = max(stones)
    while low < high:
        middle = (low + high + 1) // 2
        if can_cross(middle):
            low = middle
        else:
            high = middle - 1
    return low
