# 🧩 피로도

- Programmers ID: 87946
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/87946
- Level: 2
- Stage: Level 2 Core 21
- Prerequisites: 20 후보 탐색, 리스트 인덱싱, 두 값 나누어 받기
- Core concepts: 순열, 완전탐색

## 🎯 이 문제에서 배우는 것

고정된 한 순서가 실패할 수 있는 문제에서 가능한 순서를 모두 확인합니다.

## 🔎 문제 핵심

현재 피로도 k와 dungeons의 [최소 필요 피로도, 소모 피로도]가 주어집니다. 각 던전은 한 번만 갈 수 있을 때 탐험 가능한 던전 수의 최댓값을 돌려줍니다.

## 💭 먼저 생각해 보기

피로도 30에서 [30, 10]과 [20, 20]을 어느 순서로 가야 두 곳을 모두 갈 수 있나요?

## 🧪 예제 이해하기

k = 30, dungeons = [[30, 10], [20, 20]]이면 첫 던전을 간 뒤 20이 남아 두 번째도 갑니다. 반대 순서에서는 10이 남아 첫 던전에 못 가므로 답은 2입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

던전 인덱스를 모든 가능한 순서로 배열합니다. 각 순서의 앞에서부터 피로도를 확인하며 가능한 개수를 세고 최댓값을 남깁니다.

### 🐍 Python 코드

```python
from itertools import permutations


def solution(k, dungeons):
    best = 0
    for order in permutations(range(len(dungeons))):
        fatigue = k
        explored = 0
        for index in order:
            required, consumed = dungeons[index]
            if fatigue < required:
                break
            fatigue -= consumed
            explored += 1
        best = max(best, explored)
    return best
```

### 📖 코드 해설

순열은 같은 항목들을 다른 순서로 놓은 경우들입니다. itertools.permutations()는 가능한 순서를 하나씩 내줍니다. 모든 순서에는 최적 탐험 순서를 맨 앞에 놓은 경우도 있습니다. 그래서 못 들어가는 던전에서 멈춰도 최대 개수를 놓치지 않습니다. 각 순서마다 원래 k로 다시 시작합니다. 값이 같은 던전도 위치가 다르면 다른 던전입니다.

### ⏱️ 시간 복잡도

던전 수를 N이라 하면 순서가 N!개이고 각 순서에 최대 N개를 확인해 O(N × N!)입니다. N!은 1×2×…×N이며 이 문제의 N은 최대 8이라 전부 살필 수 있습니다.

### 💾 공간 복잡도

순열을 한 번에 한 개씩 받아 현재 순서와 내부 상태에 O(N)을 씁니다. 모든 순열을 리스트로 모으지 않으며 반환값 포함입니다.

## ⚠️ 실수하기 쉬운 점

- 필요 피로도를 소모량처럼 빼지 않습니다.
- 한 순서의 피로도를 다음 순서까지 이어 쓰지 않습니다.

## ✅ 배운 것

가능한 순서 수가 작다면 모든 순서를 확인해 한 기준으로 정렬할 때 놓친 답을 찾을 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 한 기준으로 정렬하는 방법이 실패하는 예를 설명하기

## 🚀 이어 풀어 볼 문제

- [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) (`42839`) — 숫자 조각의 가능한 순서도 모두 확인합니다.
- [모음사전](https://school.programmers.co.kr/learn/courses/30/lessons/84512) (`84512`) — 짧은 후보들을 일정한 순서로 만들어 봅니다.
