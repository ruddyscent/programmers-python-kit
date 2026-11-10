# 🧩 가장 먼 노드

- Programmers ID: 49189
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/49189
- Level: 3
- Stage: Level 3 Core 16
- Prerequisites: 15 BFS, Level 2 26 이웃 리스트, count()
- Core concepts: 인접 리스트, BFS 거리 기록

## 🎯 이 문제에서 배우는 것

연결된 점만 저장하는 인접 리스트로 그래프를 만들고 BFS로 모든 거리를 구합니다.

## 🔎 문제 핵심

1번부터 n번까지 노드가 있고 edge의 각 항목은 양쪽으로 오갈 수 있는 간선입니다. 1번 노드에서 지나는 간선 수가 가장 많이 필요한 노드, 곧 가장 멀리 있는 노드가 몇 개인지 돌려줍니다.

## 💭 먼저 생각해 보기

1번에서 한 번에 갈 수 있는 노드에 1, 거기서 처음 닿는 노드에 2를 적어 보세요. 가장 큰 숫자가 적힌 노드는 몇 개인가요?

## 🧪 예제 이해하기

n = 5, edge = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]]이면 거리는 2와 3이 1, 4가 2, 5가 3입니다. 가장 먼 노드는 5 하나라 결과는 1입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

노드마다 이웃 목록을 만듭니다. 1번에서 BFS를 하며 처음 도착한 거리를 기록하고 가장 큰 거리의 개수를 셉니다.

### 🐍 Python 코드

```python
from collections import deque


def solution(n, edge):
    neighbors = []
    for node in range(n + 1):
        neighbors.append([])
    for first, second in edge:
        neighbors[first].append(second)
        neighbors[second].append(first)

    distances = [-1] * (n + 1)
    distances[1] = 0
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor in neighbors[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    farthest = max(distances)
    return distances.count(farthest)
```

### 📖 코드 해설

neighbors[node]에는 node와 직접 연결된 노드들만 들어 있습니다. 이런 모양을 인접 리스트라고 합니다. 14번의 인접 행렬은 n × n 칸이 필요하지만 인접 리스트는 실제 간선 수만큼만 저장합니다. 노드가 2만 개라면 행렬은 4억 칸이라 너무 큽니다. 간선은 양쪽으로 오가므로 양쪽 목록에 모두 넣습니다. distances의 -1은 아직 방문하지 않았다는 표시입니다. 0번 칸은 쓰지 않지만 -1이라 최댓값 계산에 영향을 주지 않습니다.

### ⏱️ 시간 복잡도

노드 수를 N, 간선 수를 E라 합니다. 이웃 목록을 만드는 데 O(N + E), BFS에서 각 노드와 간선을 한 번씩 보는 데 O(N + E)가 걸립니다. max()와 count()는 O(N)이라 전체 O(N + E)입니다.

### 💾 공간 복잡도

이웃 목록에 O(N + E), 거리와 큐에 O(N)을 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 간선을 한쪽 방향만 넣으면 반대쪽에서 갈 수 없게 됩니다.
- 노드 번호가 1부터라 리스트를 n + 1칸으로 만듭니다.

## ✅ 배운 것

간선이 노드 수에 비해 적은 그래프는 인접 리스트로 저장하고, BFS 한 번으로 모든 노드의 거리를 구합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 가장 먼 노드가 여러 개인 예 확인하기

## 🚀 이어 풀어 볼 문제

- [부대복귀](https://school.programmers.co.kr/learn/courses/30/lessons/132266) (`132266`) — 여러 출발점의 거리를 BFS 한 번으로 구합니다.
- [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) (`43162`) — 인접 행렬과 인접 리스트의 차이를 비교합니다.
