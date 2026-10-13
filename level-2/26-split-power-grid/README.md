# 🧩 전력망을 둘로 나누기

- Programmers ID: 86971
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/86971
- Level: 2
- Stage: Level 2 Core 26
- Prerequisites: 25 BFS, 리스트 순회
- Core concepts: 그래프, 트리, 간선 제외

## 🎯 이 문제에서 배우는 것

한 연결을 제외한 뒤 연결된 지점 수를 세어 두 묶음의 크기를 비교합니다.

## 🔎 문제 핵심

n개 송전탑을 잇는 트리의 전선 wires 중 하나를 끊습니다. 나뉜 두 전력망의 송전탑 수 차이의 최솟값을 돌려줍니다.

## 💭 먼저 생각해 보기

1-2-3-4-5가 일렬로 연결되어 있습니다. 가운데 연결을 끊을 때와 끝 연결을 끊을 때 묶음 크기를 비교하세요.

## 🧪 예제 이해하기

n = 5, wires = [[1,2], [2,3], [3,4], [4,5]]에서 2-3을 끊으면 2개와 3개라 차이는 1입니다. 더 작은 차이는 없으므로 결과는 1입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

각 탑에 연결된 이웃 목록을 만듭니다. 전선을 하나씩 제외하고 그 한쪽에서 BFS로 셉니다. 반대 묶음은 전체에서 방문 수를 뺀 값입니다.

### 🐍 Python 코드

```python
from collections import deque


def solution(n, wires):
    neighbors = []
    for node in range(n + 1):
        neighbors.append([])
    for first, second in wires:
        neighbors[first].append(second)
        neighbors[second].append(first)

    best = n
    for cut_first, cut_second in wires:
        visited = [False] * (n + 1)
        visited[cut_first] = True
        queue = deque([cut_first])
        connected = 0
        while queue:
            node = queue.popleft()
            connected += 1
            for neighbor in neighbors[node]:
                is_cut = (node == cut_first and neighbor == cut_second)
                is_cut = is_cut or (node == cut_second and neighbor == cut_first)
                if is_cut or visited[neighbor]:
                    continue
                visited[neighbor] = True
                queue.append(neighbor)
        best = min(best, abs(n - 2 * connected))
    return best
```

### 📖 코드 해설

지점을 노드, 연결을 간선이라 부르는 자료가 그래프입니다. 이웃 목록은 어느 지점과 직접 연결되었는지 기록합니다. 트리는 전체가 연결되고 돌아서 같은 곳에 오는 순환이 없습니다. 그래서 전선 하나를 끊으면 정확히 둘로 나뉩니다. 방문 수가 connected면 두 크기는 connected와 n-connected이고 차이는 abs(n-2*connected)입니다. 실제 wires를 지우지 않고 양 방향을 건너뜁니다.

### ⏱️ 시간 복잡도

탑 수 N의 트리는 전선이 N-1개입니다. 전선 후보마다 BFS와 방문 배열에 O(N)이 들어 전체 O(N²)입니다.

### 💾 공간 복잡도

이웃 목록, 방문 배열, 큐에 각각 O(N)을 씁니다. 후보마다 배열을 새로 만들지만 이전 배열을 모두 모으지 않아 반환값 포함 추가 공간은 O(N)입니다.

## ⚠️ 실수하기 쉬운 점

- 전선은 양방향이므로 이웃 목록에 두 방향을 넣습니다.
- 이 방문 계산을 일반 순환 그래프에 적용해도 반드시 두 묶음으로 나뉘는 것은 아닙니다.

## ✅ 배운 것

이웃 목록으로 연결을 저장하고 특정 간선을 제외하며 연결된 지점 수를 셉니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 일렬 연결과 한 탑에 모두 연결된 모양을 비교하기

## 🚀 이어 풀어 볼 문제

- [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) (`1844`) — 큐에 넣을 때 방문 표시하는 BFS를 복습합니다.
- [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) (`87946`) — 후보 하나마다 새 상태로 다시 시도합니다.
