def solution(n, costs):
    leader = list(range(n))

    def find(island):
        while leader[island] != island:
            island = leader[island]
        return island

    def bridge_cost(bridge):
        return bridge[2]

    total = 0
    bridges = 0
    for first, second, cost in sorted(costs, key=bridge_cost):
        first_leader = find(first)
        second_leader = find(second)
        if first_leader == second_leader:
            continue
        leader[second_leader] = first_leader
        total += cost
        bridges += 1
        if bridges == n - 1:
            break
    return total
