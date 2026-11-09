# 🧩 순위

- Programmers ID: 49191
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/49191
- Level: 3
- Stage: Level 3 Core 20
- Prerequisites: 2차원 리스트, 세 중첩 반복
- Core concepts: 관계 전파, 플로이드 와샬

## 🎯 이 문제에서 배우는 것

"A가 B를 이기고 B가 C를 이기면 A가 C를 이긴다"는 관계를 표 전체로 퍼뜨립니다.

## 🔎 문제 핵심

선수 n명의 실력이 모두 다르고 실력이 높은 선수가 항상 이깁니다. results의 각 항목은 [이긴 선수, 진 선수]입니다. 일부 결과만 주어질 때 순위를 정확히 알 수 있는 선수의 수를 돌려줍니다.

## 💭 먼저 생각해 보기

어떤 선수의 순위를 알려면 나머지 선수 모두와의 승패를 알아야 할까요? 직접 경기하지 않았어도 승패를 알 수 있는 경우는 언제인가요?

## 🧪 예제 이해하기

n = 3, results = [[1, 2], [2, 3]]이면 1이 2를, 2가 3을 이겼으므로 1이 3도 이깁니다. 세 선수 모두 나머지 두 명과의 승패를 알아 결과는 3입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

wins[a][b]를 a가 b를 이긴다는 표시로 둡니다. 가운데 선수 middle을 하나씩 정해, a가 middle을 이기고 middle이 b를 이기면 a가 b를 이긴다고 표시합니다. 다 채운 뒤 이기거나 지는 관계를 아는 상대가 n - 1명인 선수를 셉니다.

### 🐍 Python 코드

```python
def solution(n, results):
    wins = []
    for player in range(n + 1):
        wins.append([False] * (n + 1))
    for winner, loser in results:
        wins[winner][loser] = True

    for middle in range(1, n + 1):
        for winner in range(1, n + 1):
            if not wins[winner][middle]:
                continue
            for loser in range(1, n + 1):
                if wins[middle][loser]:
                    wins[winner][loser] = True

    ranked = 0
    for player in range(1, n + 1):
        known = 0
        for other in range(1, n + 1):
            if wins[player][other] or wins[other][player]:
                known += 1
        if known == n - 1:
            ranked += 1
    return ranked
```

### 📖 코드 해설

가장 바깥 반복이 middle입니다. middle을 1번부터 차례로 늘리면, 지금까지 본 선수들을 거치는 모든 승리 관계가 표에 채워집니다. 그래서 반복이 끝나면 몇 명을 거치든 연결되는 승리가 모두 기록됩니다. 이처럼 거쳐 가는 점을 바깥에 두고 표를 갱신하는 방법을 플로이드 와샬 알고리즘이라고 합니다.

if not wins[winner][middle]: continue는 winner가 middle을 이기지 않으면 안쪽 반복을 건너뛰어 일을 줄입니다. 결과는 같습니다.

```text
       1  2  3
1      .  o  o   <- 2를 거쳐 3도 이김
2      .  .  o
3      .  .  .
```

### ⏱️ 시간 복잡도

선수 수를 n이라 하면 세 겹 반복이 O(n³), 마지막 확인이 O(n²)라 전체 O(n³)입니다. n이 100 이하라 100만 번 정도입니다.

### 💾 공간 복잡도

(n + 1) × (n + 1) 표를 만들어 O(n²)를 사용합니다.

## ⚠️ 실수하기 쉬운 점

- middle 반복을 가장 안쪽에 두면 관계가 다 퍼지지 않을 수 있습니다.
- 이긴 관계와 진 관계를 모두 세야 합니다. wins[other][player]도 확인합니다.

## ✅ 배운 것

거쳐 가는 선수를 하나씩 늘리며 표를 갱신하면 간접 관계까지 모두 알 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 아무 결과도 연결되지 않은 선수가 있는 예 확인하기

## 🚀 이어 풀어 볼 문제

- [행렬의 곱셈](https://school.programmers.co.kr/learn/courses/30/lessons/12949) (`12949`) — 세 중첩 반복으로 표를 계산한 경험을 복습합니다.
- [합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413) (`72413`) — 같은 방법으로 모든 지점 사이의 최소 요금을 구할 수도 있습니다.
