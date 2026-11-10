def solution(enroll, referral, seller, amount):
    parent = {}
    profit = {}
    for index in range(len(enroll)):
        parent[enroll[index]] = referral[index]
        profit[enroll[index]] = 0

    for index in range(len(seller)):
        person = seller[index]
        money = amount[index] * 100
        while person != "-" and money > 0:
            share = money // 10
            profit[person] += money - share
            person = parent[person]
            money = share

    answer = []
    for name in enroll:
        answer.append(profit[name])
    return answer
