# 🧩 더 맵게

- Programmers ID: 42626
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42626
- Level: 2
- Stage: Level 2 Core 16
- Prerequisites: 리스트 복사, while, 조건문
- Core concepts: 최소 힙, 가장 작은 두 값

## 🎯 이 문제에서 배우는 것

반복해서 가장 작은 값을 꺼내는 상황에 맞는 자료구조를 사용합니다.

## 🔎 문제 핵심

scoville의 가장 작은 두 값을 a, b라 할 때 a + 2*b로 섞습니다. 모두 K 이상이 될 때까지 필요한 섞기 횟수를 돌려주고 불가능하면 -1입니다.

## 💭 먼저 생각해 보기

[1, 4, 6]에서 목표가 10이면 먼저 어느 두 값을 섞어야 하나요? 새 값이 들어오면 다음 두 값은 달라지나요?

## 🧪 예제 이해하기

1과 4를 섞어 9가 되어 [6, 9]가 남습니다. 다음에 6과 9를 섞어 24가 됩니다. 두 번이라 결과는 2입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

리스트를 최소 힙으로 만듭니다. 가장 작은 값이 K보다 작으면 두 값을 꺼내 섞고 다시 넣습니다. 꺼낼 값이 하나만 남아 부족하면 실패입니다.

### 🐍 Python 코드

```python
from heapq import heapify, heappop, heappush


def solution(scoville, K):
    foods = scoville[:]
    heapify(foods)
    mixed = 0
    while foods[0] < K:
        if len(foods) < 2:
            return -1
        first = heappop(foods)
        second = heappop(foods)
        heappush(foods, first + 2 * second)
        mixed += 1
    return mixed
```

### 📖 코드 해설

최소 힙은 맨 앞에서 최솟값을 읽을 수 있도록 값을 배치한 자료구조입니다. 전체가 정렬된 리스트는 아닙니다. heapify()가 배치를 만들고 heappop()과 heappush()는 값을 꺼내거나 넣은 뒤 이 성질을 유지합니다. scoville[:]를 복사해 입력을 보존합니다. 문제의 입력은 비어 있지 않습니다.

### ⏱️ 시간 복잡도

음식 수를 N이라 하면 heapify는 O(N), 꺼내기와 넣기는 한 번에 O(log N)입니다. 섞을 때 개수가 하나 줄어 최대 N-1번 섞으므로 전체 O(N log N)입니다.

### 💾 공간 복잡도

복사한 힙 리스트에 N개의 값을 저장합니다. 반환값을 포함해 추가 공간은 O(N)입니다.

## ⚠️ 실수하기 쉬운 점

- 가장 작은 값이 이미 K 이상이면 섞지 않습니다.
- 힙의 두 번째 칸이 두 번째 최솟값이라고 가정하지 말고 두 번 꺼냅니다.

## ✅ 배운 것

최소 힙은 전체를 다시 정렬하지 않고 최솟값을 반복해서 꺼내고 넣는 데 맞습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 처음부터 모두 충분한 경우와 끝내 부족한 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [프로세스](https://school.programmers.co.kr/learn/courses/30/lessons/42587) (`42587`) — 필요한 우선순위를 먼저 처리합니다.
- [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747) (`42747`) — 전체를 정렬할 때와 힙으로 갱신할 때를 비교합니다.
