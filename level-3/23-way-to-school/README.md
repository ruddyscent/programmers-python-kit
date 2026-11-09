# 🧩 등굣길

- Programmers ID: 42898
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42898
- Level: 3
- Stage: Level 3 Core 23
- Prerequisites: 22 동적 계획법, 2차원 리스트, set()
- Core concepts: 격자 경로 수, 나머지 연산

## 🎯 이 문제에서 배우는 것

각 칸까지 가는 경로 수를 위쪽과 왼쪽 칸에서 더해 구합니다.

## 🔎 문제 핵심

가로 m칸, 세로 n칸 격자에서 집은 (1, 1), 학교는 (m, n)입니다. 오른쪽이나 아래쪽으로만 움직이며 puddles의 물웅덩이는 지날 수 없습니다. puddles의 각 항목은 [가로 위치, 세로 위치]입니다. 집에서 학교까지 가장 짧은 경로의 수를 1,000,000,007로 나눈 나머지로 돌려줍니다.

## 💭 먼저 생각해 보기

오른쪽과 아래로만 가면 모든 경로의 길이가 같습니다. 어떤 칸에 도착하는 방법은 바로 위 칸과 바로 왼쪽 칸 중 어디에서 오는 경우로 나눌 수 있을까요?

## 🧪 예제 이해하기

m = 3, n = 2이고 웅덩이가 없으면 (3, 2)까지 경로는 3개입니다. 웅덩이가 [2, 1]에 있으면 윗줄 가운데를 지날 수 없습니다. 아래로 먼저 내려간 뒤 오른쪽으로 가는 경로 하나만 남아 결과는 1입니다.

```text
웅덩이 없음        [2, 1]에 웅덩이
1 1 1              1 X 0
1 2 3              1 1 1
```

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

ways[row][column]은 그 칸까지 오는 경로 수입니다. 집은 1이고 웅덩이는 0이며 나머지는 위 칸과 왼쪽 칸의 값을 더합니다.

### 🐍 Python 코드

```python
def solution(m, n, puddles):
    divisor = 1000000007
    flooded = set()
    for column, row in puddles:
        flooded.add((row, column))

    ways = []
    for row in range(n + 1):
        ways.append([0] * (m + 1))
    ways[1][1] = 1

    for row in range(1, n + 1):
        for column in range(1, m + 1):
            if row == 1 and column == 1:
                continue
            if (row, column) in flooded:
                continue
            ways[row][column] = (ways[row - 1][column] + ways[row][column - 1]) % divisor
    return ways[n][m]
```

### 📖 코드 해설

리스트를 (n + 1) × (m + 1)로 만들어 번호를 1부터 그대로 씁니다. 0번 행과 0번 열은 모두 0이라 맨 윗줄과 맨 왼쪽 줄도 같은 식으로 계산됩니다. puddles는 [가로, 세로] 순서라 (row, column) 튜플로 바꿔 집합에 넣습니다. 웅덩이 칸은 continue로 건너뛰어 0으로 남습니다.

경로 수는 매우 커질 수 있습니다. 더할 때마다 1,000,000,007로 나눈 나머지만 남겨도 마지막 나머지는 같습니다.

### ⏱️ 시간 복잡도

칸 수 m × n만큼 한 번씩 계산해 O(mn)입니다. 웅덩이 수를 P라 하면 집합을 만드는 데 O(P)가 더 듭니다.

### 💾 공간 복잡도

ways 표에 O(mn), 웅덩이 집합에 O(P)를 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 문제의 좌표는 [가로, 세로]입니다. 리스트의 [행][열]과 순서가 반대입니다.
- 마지막에만 나머지를 구해도 Python에서는 맞지만 수가 매우 커져 느려집니다. 더할 때마다 나머지를 구합니다.

## ✅ 배운 것

한 칸으로 들어오는 방향이 정해져 있으면 들어오는 칸들의 경로 수를 더해 표를 채웁니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 웅덩이 때문에 학교까지 갈 수 없는 예 확인하기

## 🚀 이어 풀어 볼 문제

- [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105) (`43105`) — 위층에서 오는 값을 이어 계산하는 DP를 복습합니다.
- [거스름돈](https://school.programmers.co.kr/learn/courses/30/lessons/12907) (`12907`) — 경우의 수를 표에 더하는 다른 DP를 연습합니다.
