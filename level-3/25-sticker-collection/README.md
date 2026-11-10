# 🧩 스티커 모으기(2)

- Programmers ID: 12971
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/12971
- Level: 3
- Stage: Level 3 Core 25
- Prerequisites: 22 동적 계획법, 슬라이싱
- Core concepts: 고르거나 건너뛰기 DP, 원형을 두 줄로 나누기

## 🎯 이 문제에서 배우는 것

원형으로 이어진 문제를 첫 칸과 마지막 칸 중 하나를 뺀 두 줄 문제로 바꿉니다.

## 🔎 문제 핵심

원형으로 이어진 스티커에 숫자가 있습니다. 스티커 하나를 뜯으면 양옆 스티커는 쓸 수 없습니다. 첫 스티커와 마지막 스티커도 서로 이웃입니다. 뜯은 스티커 숫자 합의 최댓값을 돌려줍니다.

## 💭 먼저 생각해 보기

한 줄로 놓인 스티커라면 i번째까지의 최대 합은 어떻게 정할까요? i번째를 뜯는 경우와 뜯지 않는 경우로 나눠 보세요. 원형이라 생기는 문제는 첫 칸과 마지막 칸을 둘 다 뜯는 경우뿐입니다.

## 🧪 예제 이해하기

sticker = [5, 1, 3, 6]입니다. 마지막을 뺀 [5, 1, 3]에서는 5 + 3 = 8, 첫 칸을 뺀 [1, 3, 6]에서는 1 + 6 = 7이 최대입니다. 결과는 8입니다. 원형이 아니라면 5 + 6 = 11이 가능하지만 처음과 끝이 이웃이라 안 됩니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

한 줄에서 현재까지의 최대 합은 "직전까지의 최대 합"과 "두 칸 전까지의 최대 합 + 현재 값" 중 큰 값입니다. 원형에서는 마지막을 뺀 줄과 첫 칸을 뺀 줄을 각각 계산해 큰 값을 고릅니다.

### 🐍 Python 코드

```python
def solution(sticker):
    def best_in_line(values):
        before_previous = 0
        previous = 0
        for value in values:
            current = max(previous, before_previous + value)
            before_previous = previous
            previous = current
        return previous

    if len(sticker) == 1:
        return sticker[0]
    without_last = best_in_line(sticker[:-1])
    without_first = best_in_line(sticker[1:])
    return max(without_last, without_first)
```

### 📖 코드 해설

best_in_line은 표 전체 대신 직전 값 previous와 두 칸 전 값 before_previous만 기억합니다. current를 계산한 뒤 두 값을 한 칸씩 앞으로 옮깁니다. 첫 칸과 마지막 칸은 동시에 뜯을 수 없으므로 최적의 답은 둘 중 하나를 쓰지 않습니다. 그래서 두 줄의 답 중 큰 값이 원형의 답입니다. 스티커가 하나뿐이면 두 슬라이스가 모두 비므로 따로 처리합니다.

```text
값          5  1  3
previous    5  5  8
```

### ⏱️ 시간 복잡도

스티커 수를 N이라 하면 슬라이싱이 O(N), 두 번의 계산이 O(N)이라 전체 O(N)입니다.

### 💾 공간 복잡도

sticker[:-1]과 sticker[1:]가 새 리스트를 만들어 O(N)을 사용합니다. 슬라이스 대신 시작과 끝 위치를 넘기면 O(1)로 줄일 수 있습니다.

## ⚠️ 실수하기 쉬운 점

- 짝수 번째나 홀수 번째만 모두 뜯는 방법은 답이 아닐 수 있습니다. 두 칸 이상 건너뛰는 편이 나을 때가 있습니다.
- 스티커가 한 장인 경우를 빼먹기 쉽습니다.

## ✅ 배운 것

원형 조건 때문에 생기는 충돌을 두 경우로 나누면 한 줄 DP를 그대로 쓸 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 스티커가 1장, 2장, 3장인 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701) (`131701`) — 원형 수열을 다루는 다른 방법을 복습합니다.
- [연속 펄스 부분 수열의 합](https://school.programmers.co.kr/learn/courses/30/lessons/161988) (`161988`) — 직전 값 몇 개만 기억하는 DP를 이어서 연습합니다.
