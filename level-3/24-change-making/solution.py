def solution(n, money):
    divisor = 1000000007
    ways = [0] * (n + 1)
    ways[0] = 1
    for coin in money:
        for price in range(coin, n + 1):
            ways[price] = (ways[price] + ways[price - coin]) % divisor
    return ways[n]
