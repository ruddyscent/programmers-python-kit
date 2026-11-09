# 🧩 부대복귀

- Programmers ID: 132266
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/132266
- Level: 3
- Stage: Level 3 Core 17
- Prerequisites: 16 인접 리스트와 BFS
- Core concepts: 도착점에서 거꾸로 BFS

## 🎯 이 문제에서 배우는 것

여러 출발점의 거리를 구할 때 공통 도착점에서 한 번만 BFS하는 방법을 배웁니다.

## 🔎 문제 핵심

지역 1~n과 양방향 길 roads가 있습니다. 길 하나를 지나는 데 1이 걸립니다. sources의 각 지역에서 destination까지의 최단 시간을 sources 순서대로 돌려주고 갈 수 없으면 -1을 넣습니다.

## 💭 먼저 생각해 보기

출발점이 500개라면 BFS를 500번 해야 할까요? 길이 양방향이라면 A에서 B까지 거리와 B에서 A까지 거리는 어떤 관계인가요?

## 🧪 예제 이해하기

n = 4, roads = [[1, 2], [2, 3]], sources = [1, 3, 4], destination = 2입니다. 2에서 BFS를 하면 1과 3은 거리 1, 4는 닿지 않습니다. 결과는 [1, 1, -1]입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

길이 양방향이라 destination에서 각 지역까지의 거리가 각 지역에서 destination까지의 거리와 같습니다. destination에서 BFS를 한 번 하고 sources의 거리를 읽습니다.

### 🐍 Python 코드

```python
from collections import deque


def solution(n, roads, sources, destination):
    neighbors = []
    for area in range(n + 1):
        neighbors.append([])
    for first, second in roads:
        neighbors[first].append(second)
        neighbors[second].append(first)

    distances = [-1] * (n + 1)
    distances[destination] = 0
    queue = deque([destination])
    while queue:
        area = queue.popleft()
        for neighbor in neighbors[area]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[area] + 1
                queue.append(neighbor)

    answer = []
    for source in sources:
        answer.append(distances[source])
    return answer
```

### 📖 코드 해설

16번과 같은 인접 리스트와 BFS입니다. 출발점을 destination으로 바꾼 것만 다릅니다. distances의 초깃값 -1은 닿지 않은 지역의 답으로 그대로 쓰입니다. destination 자신이 sources에 있으면 거리 0이 들어갑니다.

### ⏱️ 시간 복잡도

지역 수를 N, 길 수를 E, 출발점 수를 S라 합니다. BFS 한 번이 O(N + E), 답을 읽는 데 O(S)라 전체 O(N + E + S)입니다. 출발점마다 BFS를 하면 O(S(N + E))로 훨씬 많아집니다.

### 💾 공간 복잡도

이웃 목록에 O(N + E), 거리와 큐에 O(N), 반환값에 O(S)를 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 출발점마다 BFS를 반복하면 입력이 클 때 시간이 부족합니다.
- 길이 한 방향이라면 거꾸로 BFS할 때 간선 방향도 뒤집어야 합니다. 이 문제는 양방향입니다.

## ✅ 배운 것

출발점은 여럿이고 도착점이 하나면 도착점에서 거꾸로 탐색해 한 번에 모든 거리를 구할 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 출발점이 도착점과 같은 경우와 고립된 지역 확인하기

## 🚀 이어 풀어 볼 문제

- [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189) (`49189`) — 한 점에서 BFS로 거리를 기록하는 방법을 복습합니다.
- [합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413) (`72413`) — 길마다 비용이 다를 때 거리를 구합니다.
