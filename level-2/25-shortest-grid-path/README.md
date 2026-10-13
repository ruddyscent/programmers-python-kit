# 🧩 게임 맵 최단거리

- Programmers ID: 1844
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/1844
- Level: 2
- Stage: Level 2 Core 25
- Prerequisites: 14 deque, 리스트 인덱싱, 반복문
- Core concepts: BFS, 방문 거리 기록

## 🎯 이 문제에서 배우는 것

가까운 칸부터 방문하는 순서로 가장 짧은 경로를 찾습니다.

## 🔎 문제 핵심

0은 벽, 1은 길인 maps에서 왼쪽 위부터 오른쪽 아래까지 네 방향으로 이동합니다. 지나간 칸 수의 최솟값을 돌려주고 못 가면 -1입니다. 시작 칸도 셉니다.

## 💭 먼저 생각해 보기

[[1, 1, 0], [0, 1, 1]]에서 시작을 1로 표시하고 한 걸음으로 갈 수 있는 칸에 다음 수를 적어 보세요.

## 🧪 예제 이해하기

위 지도에서는 (0,0), (0,1), (1,1), (1,2)로 지나가 4칸입니다. 결과는 4입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

시작 칸의 거리를 1로 기록하고 큐에 넣습니다. 큐에서 꺼낸 칸의 아직 방문하지 않은 이웃에 거리+1을 기록하고 넣습니다.

### 🐍 Python 코드

```python
from collections import deque


def solution(maps):
    rows = len(maps)
    columns = len(maps[0])
    distances = []
    for row in range(rows):
        distances.append([-1] * columns)
    distances[0][0] = 1
    queue = deque([(0, 0)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        row, column = queue.popleft()
        if row == rows - 1 and column == columns - 1:
            return distances[row][column]
        for row_change, column_change in directions:
            next_row = row + row_change
            next_column = column + column_change
            if not (0 <= next_row < rows and 0 <= next_column < columns):
                continue
            if maps[next_row][next_column] == 0:
                continue
            if distances[next_row][next_column] != -1:
                continue
            distances[next_row][next_column] = distances[row][column] + 1
            queue.append((next_row, next_column))
    return -1
```

### 📖 코드 해설

2차원 리스트는 행 리스트들을 담은 리스트입니다. distances[row][column]처럼 행, 열 순서로 읽습니다. 행마다 새 리스트를 만들어 서로 독립적으로 바뀌게 합니다. BFS(너비 우선 탐색)는 큐로 가까운 거리부터 방문합니다. 한 걸음씩 같은 비용이어서 먼저 도착한 거리가 최솟값입니다. 넣을 때 방문을 표시해 같은 칸을 여러 번 넣지 않습니다. 지도 원본은 바꾸지 않습니다.

```text
방문 거리
1  2  벽
벽 3  4
```

### ⏱️ 시간 복잡도

행 수 R, 열 수 C에 대해 각 칸을 최대 한 번 넣고 네 이웃을 확인합니다. 시간은 O(RC)입니다.

### 💾 공간 복잡도

거리 지도와 최대 RC칸의 큐를 저장합니다. 반환값을 포함한 추가 공간은 O(RC)입니다.

## ⚠️ 실수하기 쉬운 점

- 음수 인덱스는 Python에서 뒤쪽 칸을 뜻하므로 지도 범위를 먼저 검사합니다.
- 모든 이동 비용이 같을 때의 최단거리 방법입니다. 이동 비용이 다른 문제에 그대로 적용하지 않습니다.

## ✅ 배운 것

모든 이동 비용이 같으면 큐로 가까운 칸부터 방문해 처음 도착한 최단거리를 기록할 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 우회 경로, 막힌 도착점, 가로로 긴 지도를 확인하기

## 🚀 이어 풀어 볼 문제

- [프로세스](https://school.programmers.co.kr/learn/courses/30/lessons/42587) (`42587`) — 큐 앞에서 꺼내는 연산을 복습합니다.
- [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971) (`86971`) — 연결된 지점들의 방문을 다른 문제에 적용합니다.
