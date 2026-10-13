# 🧩 타겟 넘버

- Programmers ID: 43165
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/43165
- Level: 2
- Stage: Level 2 Core 24
- Prerequisites: 23 재귀와 DFS, 합계 누적
- Core concepts: 선택의 나무, 경로별 개수

## 🎯 이 문제에서 배우는 것

같은 중간 합이 나와도 다른 선택 경로면 각각 세어야 함을 익힙니다.

## 🔎 문제 핵심

numbers의 순서를 유지하며 각 수를 더하거나 빼서 target이 되는 방법 수를 돌려줍니다.

## 💭 먼저 생각해 보기

[2, 1]에서 첫 수의 부호를 고른 뒤 다음 수에 두 선택을 붙여 보세요. 만들어지는 합은 무엇인가요?

## 🧪 예제 이해하기

numbers = [2, 1], target = 1이면 +2-1만 가능해 답은 1입니다. 수가 반복되어도 각 위치의 선택은 따로 셉니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

현재 위치와 합계를 재귀 함수에 전달합니다. 다음 수를 더하는 갈래와 빼는 갈래의 방법 수를 더합니다. 모든 수를 썼을 때 목표와 같으면 1을 돌려줍니다.

### 🐍 Python 코드

```python
def solution(numbers, target):
    def search(index, total):
        if index == len(numbers):
            if total == target:
                return 1
            return 0
        added = search(index + 1, total + numbers[index])
        subtracted = search(index + 1, total - numbers[index])
        return added + subtracted

    return search(0, 0)
```

### 📖 코드 해설

index가 한 번에 1씩 증가해 끝에서 멈춥니다. total은 각 호출의 값이라 한 갈래를 계산해도 다른 갈래의 합을 바꾸지 않습니다. 잎의 결과 1 또는 0을 부모 호출에서 더해 목표에 도달한 경로 수를 계산합니다. 깊이는 최대 20이라 문제 범위에서는 호출 깊이가 작습니다.

### ⏱️ 시간 복잡도

수의 개수 N마다 두 선택이 생겨 잎은 2^N개입니다. 모든 중간 호출까지 합해 시간은 O(2^N)입니다.

### 💾 공간 복잡도

한 번에 한 경로만 끝까지 내려갑니다. 경로의 재귀 호출 N개와 반환값을 포함한 추가 공간은 O(N)입니다.

## ⚠️ 실수하기 쉬운 점

- 중간 합을 집합에 넣어 중복을 없애면 서로 다른 경로를 놓칩니다.
- 합이 target이 됐어도 아직 수가 남았다면 계속 선택해야 합니다.

## ✅ 배운 것

같은 합을 만드는 서로 다른 부호 경로는 서로 다른 방법으로 셉니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 같은 합으로 모이는 서로 다른 선택 경로를 그려 보기

## 🚀 이어 풀어 볼 문제

- [모음사전](https://school.programmers.co.kr/learn/courses/30/lessons/84512) (`84512`) — 재귀의 시작과 종료를 복습합니다.
- [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) (`1844`) — 깊이 우선과 가까운 곳 우선의 방문 순서를 비교합니다.
