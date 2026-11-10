# 🧩 네트워크

- Programmers ID: 43162
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/43162
- Level: 3
- Stage: Level 3 Core 14
- Prerequisites: Level 2 23 깊이 우선 탐색, 리스트를 스택으로 쓰기, 2차원 리스트
- Core concepts: 연결 요소, 인접 행렬, 반복문 DFS

## 🎯 이 문제에서 배우는 것

서로 이어진 컴퓨터 묶음이 몇 개인지 방문 기록으로 셉니다.

## 🔎 문제 핵심

컴퓨터가 n대 있고 computers[i][j]가 1이면 i와 j가 직접 연결되어 있습니다. 직접 또는 다른 컴퓨터를 거쳐 연결된 컴퓨터들을 하나의 네트워크로 볼 때 네트워크의 수를 돌려줍니다.

## 💭 먼저 생각해 보기

아직 방문하지 않은 컴퓨터 하나에서 출발해 갈 수 있는 곳을 모두 칠하면 무엇이 하나 끝난 걸까요? 다음에 칠하지 않은 컴퓨터를 만나면 무엇을 세야 하나요?

## 🧪 예제 이해하기

컴퓨터 0-1이 연결되고 2-3이 연결되어 있으며 4는 혼자입니다. 0에서 출발하면 0, 1을 칠합니다. 2에서 출발하면 2, 3을 칠합니다. 4에서 한 번 더 출발해 결과는 3입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

컴퓨터를 차례로 보며 아직 방문하지 않았으면 네트워크 수를 하나 늘리고 그 컴퓨터와 연결된 모든 컴퓨터를 방문 처리합니다.

### 🐍 Python 코드

```python
def solution(n, computers):
    visited = [False] * n
    networks = 0
    for start in range(n):
        if visited[start]:
            continue
        networks += 1
        visited[start] = True
        stack = [start]
        while stack:
            computer = stack.pop()
            for neighbor in range(n):
                if computers[computer][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
    return networks
```

### 📖 코드 해설

stack은 앞으로 이웃을 살펴볼 컴퓨터 목록입니다. pop()은 마지막에 넣은 컴퓨터를 꺼내므로 한 갈래를 깊이 따라갑니다. 재귀 대신 리스트로 깊이 우선 탐색(DFS)을 한 것입니다. 스택에 넣을 때 바로 방문 표시를 해 같은 컴퓨터를 여러 번 넣지 않습니다.

computers처럼 모든 두 컴퓨터의 연결 여부를 표로 저장한 것을 인접 행렬이라고 합니다. 한 컴퓨터의 이웃을 찾으려면 그 행의 n칸을 모두 봅니다. 서로 연결된 덩어리 하나를 연결 요소라고 부릅니다.

```text
0 - 1     2 - 3     4
[묶음 1]  [묶음 2]  [묶음 3]
```

### ⏱️ 시간 복잡도

컴퓨터 수를 n이라 하면 각 컴퓨터를 한 번 꺼내 행의 n칸을 확인하므로 O(n²)입니다.

### 💾 공간 복잡도

방문 기록과 스택에 O(n)을 사용합니다.

## ⚠️ 실수하기 쉬운 점

- computers[i][i]는 항상 1입니다. 자기 자신을 연결로 세어도 방문 기록 덕분에 문제는 없습니다.
- 연결 개수를 세는 것이 아니라 덩어리 개수를 셉니다.

## ✅ 배운 것

방문하지 않은 곳에서 탐색을 새로 시작한 횟수가 연결 요소의 수입니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 모두 연결된 경우와 모두 떨어진 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) (`42861`) — 묶음의 대표로 연결 여부를 확인합니다.
- [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189) (`49189`) — 인접 리스트로 저장한 그래프에서 거리를 셉니다.
