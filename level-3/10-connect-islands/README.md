# 🧩 섬 연결하기

- Programmers ID: 42861
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42861
- Level: 3
- Stage: Level 3 Core 10
- Prerequisites: 08 정렬 기준 함수, while, Level 2 26 그래프
- Core concepts: 최소 신장 트리, 크루스칼, 대표 찾기

## 🎯 이 문제에서 배우는 것

싼 다리부터 놓되 이미 연결된 섬 사이에는 놓지 않는 크루스칼 알고리즘을 배웁니다.

## 🔎 문제 핵심

섬 n개와 다리 후보 costs가 있습니다. costs[i]는 [섬1, 섬2, 비용]입니다. 모든 섬이 서로 오갈 수 있도록 다리를 고를 때 비용 합의 최솟값을 돌려줍니다. 다리를 여러 번 건너서 가도 연결된 것으로 봅니다.

## 💭 먼저 생각해 보기

가장 싼 다리부터 놓는다고 해 봅시다. 이미 연결된 두 섬 사이의 다리를 또 놓으면 무엇이 생기나요? 그 다리는 꼭 필요할까요?

## 🧪 예제 이해하기

섬 0, 1, 2와 다리 [0, 1, 1], [1, 2, 2], [0, 2, 3]이 있습니다. 비용 1로 0-1, 비용 2로 1-2를 놓으면 0과 2도 연결됩니다. 비용 3 다리는 필요 없어 결과는 3입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

다리를 비용 순서로 봅니다. 두 섬이 이미 같은 묶음이면 건너뛰고 다른 묶음이면 다리를 놓고 두 묶음을 합칩니다. 섬이 n개면 다리 n - 1개로 모두 연결됩니다.

### 🐍 Python 코드

```python
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
```

### 📖 코드 해설

leader[island]는 섬이 따르는 다른 섬을 가리킵니다. 자기 자신을 가리키는 섬이 그 묶음의 대표입니다. find는 대표가 나올 때까지 따라갑니다. 두 섬의 대표가 같으면 이미 연결되어 있어 다리를 놓으면 고리(사이클)만 생깁니다. 대표가 다르면 한쪽 대표가 다른 쪽 대표를 따르게 해 두 묶음을 하나로 합칩니다. 이렇게 묶음을 찾고 합치는 구조를 유니온 파인드라고 합니다.

```text
처음    0  1  2     각자 대표
0-1     0<-1  2     1의 대표는 0
1-2     0<-1  0<-2  2의 대표도 0
0-2     대표가 같아 건너뜀
```

모든 섬을 사이클 없이 잇는 다리 묶음을 신장 트리, 비용이 가장 작은 것을 최소 신장 트리라고 합니다. 싼 다리부터 고르는 이 방법은 항상 최소 신장 트리를 만든다고 알려져 있습니다.

### ⏱️ 시간 복잡도

섬 수를 n, 다리 후보 수를 E라 합니다. 정렬이 O(E log E)입니다. 이 find는 대표까지 따라가므로 한 번에 최대 O(n)이라 다리 확인은 O(En)입니다. 전체 O(E log E + En)이고 n이 100 이하라 충분히 빠릅니다.

### 💾 공간 복잡도

leader 리스트에 O(n), 정렬한 다리 리스트에 O(E)를 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 섬 번호가 아니라 대표끼리 연결해야 묶음 전체가 합쳐집니다.
- 다리 비용만 정렬하고 섬 정보를 잃어버리지 않도록 다리 전체를 정렬합니다.

## ✅ 배운 것

대표를 기록하면 두 섬이 이미 연결되었는지 빠르게 확인하고 싼 다리부터 고르는 그리디로 최소 비용 연결을 만들 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 비용이 같은 다리가 여러 개인 예를 손으로 따라가기

## 🚀 이어 풀어 볼 문제

- [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) (`43162`) — 연결된 묶음의 수를 세어 봅니다.
- [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971) (`86971`) — 트리에서 간선 하나의 역할을 살펴봅니다.
