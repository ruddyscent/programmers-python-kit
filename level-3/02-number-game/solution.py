def solution(A, B):
    team_a = sorted(A)
    team_b = sorted(B)
    wins = 0
    a_index = 0
    for b_number in team_b:
        if b_number > team_a[a_index]:
            wins += 1
            a_index += 1
    return wins
