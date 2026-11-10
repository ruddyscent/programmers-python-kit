# 🧩 정수 삼각형

- Programmers ID: 43105
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/43105
- Level: 3
- Stage: Level 3 Core 22
- Prerequisites: Level 2 28 땅따먹기, 2차원 리스트
- Core concepts: 동적 계획법, 위층 결과 재사용

## 🎯 이 문제에서 배우는 것

각 칸까지 오는 가장 큰 합만 기억하며 한 층씩 내려갑니다.

## 🔎 문제 핵심

삼각형 꼭대기에서 아래로 내려가며 숫자를 더합니다. 아래층으로 갈 때는 바로 아래 왼쪽이나 오른쪽 칸으로만 갑니다. 바닥까지 가는 경로 가운데 합의 최댓값을 돌려줍니다.

## 💭 먼저 생각해 보기

어떤 칸에 도착하려면 바로 위층의 어느 칸에서 와야 하나요? 그 두 칸에 도착하는 최대 합을 알면 이 칸의 최대 합도 알 수 있나요?

## 🧪 예제 이해하기

```text
    5
   2 7
  4 1 3
```

둘째 층은 7, 12입니다. 셋째 층 왼쪽은 7 + 4 = 11, 가운데는 max(7, 12) + 1 = 13, 오른쪽은 12 + 3 = 15입니다. 결과는 15입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

best에 윗층 각 칸까지의 최대 합을 저장합니다. 아래층 칸은 위에서 올 수 있는 칸들의 best 중 큰 값에 자기 숫자를 더합니다. 마지막 층의 최댓값이 답입니다.

### 🐍 Python 코드

```python
def solution(triangle):
    best = [triangle[0][0]]
    for row in range(1, len(triangle)):
        current = []
        for column in range(row + 1):
            if column == 0:
                from_above = best[0]
            elif column == row:
                from_above = best[column - 1]
            else:
                from_above = max(best[column - 1], best[column])
            current.append(from_above + triangle[row][column])
        best = current
    return max(best)
```

### 📖 코드 해설

row번째 층에는 row + 1개의 칸이 있습니다. 칸 column에는 위층의 column - 1번과 column번 칸에서 올 수 있습니다. 맨 왼쪽 칸은 위층 왼쪽 끝에서만, 맨 오른쪽 칸은 위층 오른쪽 끝에서만 옵니다. 한 층을 다 계산하면 best를 current로 바꿔 다음 층의 위층 정보로 씁니다.

작은 문제의 답을 저장해 두고 큰 문제의 답을 만드는 방법이 동적 계획법(DP)입니다. 모든 경로를 세면 층마다 두 갈래라 경로 수가 2^(높이 - 1)개지만, 칸마다 최대 합만 남기면 칸 수만큼만 계산합니다.

### ⏱️ 시간 복잡도

높이를 H라 하면 칸 수는 약 H²/2개이고 칸마다 한 번 계산해 O(H²)입니다.

### 💾 공간 복잡도

한 층 정보만 기억하므로 best와 current에 O(H)를 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 양 끝 칸에서 위층의 없는 칸을 읽으면 인덱스 오류가 나거나 음수 인덱스로 엉뚱한 칸을 읽습니다.
- 위에서 아래로 갈 때마다 큰 쪽만 고르는 그리디는 나중의 큰 수를 놓칠 수 있습니다.

## ✅ 배운 것

각 칸에서 필요한 정보가 위층의 최대 합뿐이면 그 값만 저장해 모든 경로를 보지 않고 답을 구합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 아래에서 위로 올라가며 푸는 방법도 말로 설명하기

## 🚀 이어 풀어 볼 문제

- [땅따먹기](https://school.programmers.co.kr/learn/courses/30/lessons/12913) (`12913`) — 행마다 최댓값을 이어 계산한 DP를 복습합니다.
- [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898) (`42898`) — 최댓값 대신 경우의 수를 이어 더합니다.
