# 🧩 야근 지수

- Programmers ID: 12927
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/12927
- Level: 3
- Stage: Level 3 Core 05
- Prerequisites: Level 2 16 최소 힙, 음수 부호
- Core concepts: 최대 힙, 가장 큰 값 줄이기

## 🎯 이 문제에서 배우는 것

Python의 최소 힙으로 가장 큰 값을 반복해서 꺼내는 방법을 배웁니다.

## 🔎 문제 핵심

works에는 남은 일의 양이 있습니다. 퇴근까지 n시간 동안 1시간에 일 1만큼 줄일 수 있습니다. 남은 일의 양을 각각 제곱해 더한 값이 야근 피로도입니다. 피로도의 최솟값을 돌려줍니다.

## 💭 먼저 생각해 보기

[5, 2]에서 한 시간 일할 수 있다면 5와 2 중 어느 것을 줄여야 제곱의 합이 더 작아질까요? 25 - 16과 4 - 1을 비교해 보세요.

## 🧪 예제 이해하기

n = 3, works = [5, 2, 4]입니다. 가장 큰 값을 하나씩 줄이면 [4, 2, 4], [3, 2, 4], [3, 2, 3]이 됩니다. 9 + 4 + 9 = 22가 결과입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

x를 1 줄이면 제곱은 2x - 1만큼 줄어듭니다. x가 클수록 많이 줄어드므로 매시간 가장 큰 일을 1 줄입니다. 가장 큰 값을 빠르게 꺼내려고 힙을 씁니다.

### 🐍 Python 코드

```python
from heapq import heapify, heappop, heappush


def solution(n, works):
    remaining = []
    for work in works:
        remaining.append(-work)
    heapify(remaining)

    for hour in range(n):
        largest = -heappop(remaining)
        if largest == 0:
            return 0
        heappush(remaining, -(largest - 1))

    fatigue = 0
    for value in remaining:
        fatigue += value * value
    return fatigue
```

### 📖 코드 해설

heapq는 가장 작은 값을 꺼내는 최소 힙만 제공합니다. 모든 값에 -를 붙여 넣으면 원래 가장 큰 값이 가장 작은 값이 됩니다. 꺼낸 뒤 다시 -를 붙여 원래 값으로 바꿉니다. 가장 큰 값이 0이면 모든 일이 끝났으므로 바로 0을 돌려줍니다. 마지막에 value × value를 계산할 때는 음수를 제곱해도 결과가 같아서 부호를 되돌리지 않았습니다.

```text
원래 값  5  2  4
힙 값   -5 -2 -4   가장 작은 -5가 원래의 가장 큰 5
```

### ⏱️ 시간 복잡도

일의 개수를 W라 하면 힙 만들기에 O(W), 한 시간마다 꺼내고 넣는 데 O(log W)가 듭니다. 전체는 O(W + n log W)입니다.

### 💾 공간 복잡도

부호를 바꾼 힙 리스트에 W개를 저장하므로 O(W)입니다.

## ⚠️ 실수하기 쉬운 점

- 일을 모두 끝낸 뒤에도 빼면 음수가 됩니다. 남은 일이 0인지 먼저 확인합니다.
- 큰 값부터 정렬해 한 번에 줄이면 줄인 뒤 순서가 바뀌는 것을 놓치기 쉽습니다.

## ✅ 배운 것

값에 -를 붙이면 최소 힙을 최대 힙처럼 쓸 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] n이 일의 총합보다 큰 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626) (`42626`) — 최소 힙의 기본 사용법을 복습합니다.
- [이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628) (`42628`) — 최솟값과 최댓값을 함께 다룹니다.
