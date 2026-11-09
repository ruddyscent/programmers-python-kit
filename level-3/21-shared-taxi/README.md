# 🧩 합승 택시 요금

- Programmers ID: 72413
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/72413
- Level: 3
- Stage: Level 3 Core 21
- Prerequisites: 16 인접 리스트, 06 힙, float("inf")
- Core concepts: 다익스트라, 갈라지는 지점 모두 보기

## 🎯 이 문제에서 배우는 것

길마다 비용이 다를 때 힙으로 최소 비용을 구하는 다익스트라 알고리즘을 배웁니다.

## 🔎 문제 핵심

지점 1~n과 양방향 택시 요금 fares([지점1, 지점2, 요금])가 있습니다. A와 B가 출발지 s에서 함께 택시를 타고 가다가 어느 지점에서 갈라져 각자 a와 b로 갑니다. 합승하지 않아도 됩니다. 두 사람 요금 합의 최솟값을 돌려줍니다.

## 💭 먼저 생각해 보기

두 사람이 지점 k에서 갈라진다면 전체 요금은 어떻게 나눠 쓸 수 있을까요? s에서 k까지, k에서 a까지, k에서 b까지의 최소 요금을 알면 될까요?

## 🧪 예제 이해하기

지점 1~4, 요금 1-2는 2, 2-3은 3, 2-4는 4, 1-3은 10이고 s = 1, a = 3, b = 4입니다. 2까지 합승하면 2 + 3 + 4 = 9입니다. 1에서 바로 갈라지면 (2 + 3) + (2 + 4) = 11입니다. 결과는 9입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

길이 양방향이라 k에서 a까지의 요금은 a에서 k까지의 요금과 같습니다. s, a, b에서 각각 다익스트라를 한 번씩 해 모든 지점까지의 최소 요금을 구합니다. 그다음 모든 k에 대해 from_s[k] + from_a[k] + from_b[k]의 최솟값을 고릅니다.

### 🐍 Python 코드

```python
from heapq import heappop, heappush


def solution(n, s, a, b, fares):
    roads = []
    for point in range(n + 1):
        roads.append([])
    for first, second, fare in fares:
        roads[first].append((second, fare))
        roads[second].append((first, fare))

    def cheapest_from(start):
        costs = [float("inf")] * (n + 1)
        costs[start] = 0
        heap = [(0, start)]
        while heap:
            cost, point = heappop(heap)
            if cost > costs[point]:
                continue
            for next_point, fare in roads[point]:
                new_cost = cost + fare
                if new_cost < costs[next_point]:
                    costs[next_point] = new_cost
                    heappush(heap, (new_cost, next_point))
        return costs

    from_s = cheapest_from(s)
    from_a = cheapest_from(a)
    from_b = cheapest_from(b)
    best = float("inf")
    for split in range(1, n + 1):
        best = min(best, from_s[split] + from_a[split] + from_b[split])
    return best
```

### 📖 코드 해설

BFS는 모든 길의 비용이 같을 때만 먼저 도착한 거리가 최소입니다. 요금이 다르면 다익스트라 알고리즘을 씁니다. 힙에 (지금까지의 요금, 지점)을 넣고 요금이 가장 작은 것부터 꺼냅니다. 꺼낸 지점에서 이웃으로 가는 요금이 기록보다 싸면 기록을 바꾸고 힙에 넣습니다.

한 지점이 다른 요금으로 힙에 여러 번 들어갈 수 있습니다. 꺼낸 요금이 기록보다 크면 이미 더 싼 길로 처리한 오래된 정보라 건너뜁니다. float("inf")는 어떤 수보다도 큰 값으로, 아직 갈 수 없다는 뜻입니다. 요금은 모두 양수입니다. 음수 요금이 있으면 다익스트라는 맞지 않습니다.

```text
s=1에서  1:0  2:2  3:5  4:6
a=3에서  1:5  2:3  3:0  4:7
b=4에서  1:6  2:4  3:7  4:0
합계     11   9    12   13   -> 최솟값 9 (k=2)
```

### ⏱️ 시간 복잡도

지점 수를 N, 요금 정보 수를 E라 합니다. 다익스트라 한 번은 O((N + E) log E)이고 세 번 합니다. 마지막 비교가 O(N)이라 전체 O((N + E) log E)입니다.

### 💾 공간 복잡도

인접 리스트에 O(N + E), 요금 기록 세 개에 O(N), 힙에 최대 O(E)를 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 합승하지 않는 경우는 k = s인 경우로 이미 포함됩니다.
- 힙에서 꺼낸 오래된 정보를 건너뛰지 않으면 같은 지점을 여러 번 처리해 느려집니다.
- s, a, b 모두에서 거리를 구해야 합니다. s에서만 구하면 k에서 a까지의 요금을 알 수 없습니다.

## ✅ 배운 것

비용이 다른 길에서는 힙으로 가장 싼 후보부터 확정하는 다익스트라를 쓰고 갈라지는 지점을 모두 확인해 조합합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 따로 가는 편이 더 싼 예를 만들어 확인하기

## 🚀 이어 풀어 볼 문제

- [부대복귀](https://school.programmers.co.kr/learn/courses/30/lessons/132266) (`132266`) — 비용이 모두 같을 때의 BFS와 비교합니다.
- [순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191) (`49191`) — 모든 쌍을 한 번에 채우는 플로이드 와샬 방법을 복습합니다.
