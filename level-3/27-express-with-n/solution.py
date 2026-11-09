def solution(N, number):
    made = [set()]
    for count in range(1, 9):
        current = set()
        current.add(int(str(N) * count))
        for left_count in range(1, count):
            right_count = count - left_count
            for left in made[left_count]:
                for right in made[right_count]:
                    current.add(left + right)
                    current.add(left - right)
                    current.add(left * right)
                    if right != 0:
                        current.add(left // right)
        if number in current:
            return count
        made.append(current)
    return -1
