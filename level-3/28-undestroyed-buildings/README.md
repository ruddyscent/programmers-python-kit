# 🧩 파괴되지 않은 건물

- Programmers ID: 92344
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/92344
- Level: 3
- Stage: Level 3 Core 28
- Prerequisites: Level 2 30 누적합, 2차원 리스트
- Core concepts: 차이 배열, 2차원 누적합

## 🎯 이 문제에서 배우는 것

넓은 직사각형에 같은 값을 여러 번 더할 때 네 모서리만 기록하고 마지막에 누적합으로 펼칩니다.

## 🔎 문제 핵심

board에는 건물의 내구도가 있습니다. skill의 각 항목은 [type, r1, c1, r2, c2, degree]이며 (r1, c1)부터 (r2, c2)까지의 직사각형에 적용됩니다. type 1은 내구도를 degree만큼 낮추고 type 2는 높입니다. 모든 skill이 끝난 뒤 내구도가 1 이상인 건물 수를 돌려줍니다.

## 💭 먼저 생각해 보기

한 줄 [0, 0, 0, 0, 0]의 1~3번 칸에 5를 더하고 싶습니다. 1번 칸에 +5, 4번 칸에 -5를 적고 왼쪽부터 누적합을 구하면 어떻게 될까요?

## 🧪 예제 이해하기

한 줄에서 1~3번 칸에 +5를 기록하면 [0, 5, 0, 0, -5]입니다. 누적합을 구하면 [0, 5, 5, 5, 0]이 되어 원하는 칸에만 5가 더해집니다. 2차원에서는 같은 일을 행 방향과 열 방향으로 두 번 합니다.

```text
직사각형 (0,0)~(1,1)에 +3 기록
+3  0 -3          가로 누적   +3 +3  0        세로 누적   3 3 0
 0  0  0     ->               0  0  0    ->              3 3 0
-3  0 +3                     -3 -3  0                    0 0 0
```

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

skill마다 직사각형 전체를 고치지 않고 네 모서리에만 값을 적습니다. 모든 skill을 기록한 뒤 가로 누적합과 세로 누적합을 차례로 구하면 각 칸의 총 변화량이 나옵니다.

### 🐍 Python 코드

```python
def solution(board, skill):
    rows = len(board)
    columns = len(board[0])
    changes = []
    for row in range(rows + 1):
        changes.append([0] * (columns + 1))

    for kind, r1, c1, r2, c2, degree in skill:
        if kind == 1:
            amount = -degree
        else:
            amount = degree
        changes[r1][c1] += amount
        changes[r1][c2 + 1] -= amount
        changes[r2 + 1][c1] -= amount
        changes[r2 + 1][c2 + 1] += amount

    for row in range(rows + 1):
        for column in range(1, columns + 1):
            changes[row][column] += changes[row][column - 1]
    for row in range(1, rows + 1):
        for column in range(columns + 1):
            changes[row][column] += changes[row - 1][column]

    standing = 0
    for row in range(rows):
        for column in range(columns):
            if board[row][column] + changes[row][column] > 0:
                standing += 1
    return standing
```

### 📖 코드 해설

changes는 board보다 한 행, 한 열 크게 만들어 r2 + 1, c2 + 1 위치에 적을 때 범위를 넘지 않게 했습니다. 왼쪽 위에 +amount, 오른쪽 위 바깥과 왼쪽 아래 바깥에 -amount, 오른쪽 아래 바깥에 +amount를 적습니다. 가로로 누적하면 각 행에서 c1부터 c2까지만 값이 퍼집니다. 다시 세로로 누적하면 r1부터 r2까지만 퍼집니다. 오른쪽 아래의 +amount는 두 번 빠진 값을 되돌리는 역할입니다.

이처럼 바뀌는 경계만 기록한 표를 차이 배열이라고 합니다.

### ⏱️ 시간 복잡도

행 수를 R, 열 수를 C, skill 수를 K라 합니다. 기록에 O(K), 두 번의 누적합과 마지막 확인에 O(RC)가 걸려 전체 O(K + RC)입니다. skill마다 직사각형을 직접 고치면 O(KRC)까지 늘어납니다.

### 💾 공간 복잡도

(R + 1) × (C + 1) 크기의 changes에 O(RC)를 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 내구도가 0 이하로 떨어졌다가 다시 회복할 수 있습니다. 마지막 값만 확인합니다.
- 오른쪽 아래 바깥 칸의 +amount를 빼먹으면 직사각형 바깥 아래쪽 값이 틀어집니다.
- board 크기의 표를 만들면 r2 + 1이나 c2 + 1이 범위를 벗어날 수 있습니다.

## ✅ 배운 것

여러 구간에 같은 값을 더하는 작업은 경계만 기록하고 마지막에 한 번 누적하면 빠르게 처리할 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 직사각형이 한 칸인 경우와 board 전체인 경우를 손으로 기록하기

## 🚀 이어 풀어 볼 문제

- [연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701) (`131701`) — 1차원 누적합을 복습합니다.
- [광고 삽입](https://school.programmers.co.kr/learn/courses/30/lessons/72414) (`72414`) — 시간 구간의 시작과 끝만 기록하는 생각을 다른 문제에 적용합니다.
