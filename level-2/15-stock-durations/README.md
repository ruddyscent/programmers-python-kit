# 🧩 주식가격

- Programmers ID: 42584
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42584
- Level: 2
- Stage: Level 2 Core 15
- Prerequisites: 12 짝지어 제거하기, 인덱스와 시간 차
- Core concepts: 단조 스택, 답이 확정되는 순간

## 🎯 이 문제에서 배우는 것

아직 가격이 떨어지지 않은 시점만 기억해 새 가격에서 답을 확정합니다.

## 🔎 문제 핵심

prices의 각 시점에서 가격이 처음 떨어질 때까지의 초 수를 돌려줍니다. 끝까지 떨어지지 않으면 마지막 시점까지 셉니다. 떨어지는 순간까지의 1초도 포함합니다.

## 💭 먼저 생각해 보기

[5, 6, 4, 4]를 시간 0, 1, 2, 3 아래에 적고 각 값보다 처음으로 작은 값에 화살표를 그려 보세요.

## 🧪 예제 이해하기

[5, 6, 4, 4]의 결과는 [2, 1, 1, 0]입니다. 첫 5는 2초 뒤 4에서 떨어지고 첫 4는 끝까지 유지되어 1초입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

아직 답을 모르는 시점의 인덱스를 스택에 넣습니다. 새 가격보다 높은 끝 항목들은 지금 떨어졌으므로 꺼내 시간 차를 기록합니다. 끝까지 남은 항목은 마지막 시점까지의 차를 기록합니다.

### 🐍 Python 코드

```python
def solution(prices):
    durations = [0] * len(prices)
    waiting = []
    for current in range(len(prices)):
        while waiting and prices[waiting[-1]] > prices[current]:
            previous = waiting.pop()
            durations[previous] = current - previous
        waiting.append(current)

    last = len(prices) - 1
    for previous in waiting:
        durations[previous] = last - previous
    return durations
```

### 📖 코드 해설

waiting에는 가격이 작아지지 않는 순서로 인덱스가 쌓입니다. 이를 단조 스택이라고 부릅니다. 끝보다 높은 가격이 남아 있을 수 없으므로 뒤쪽부터 꺼내는 것만으로 이번 가격에서 떨어진 항목을 모두 처리합니다. 가격만 저장하면 언제 시작했는지 잃어서 인덱스를 저장합니다.

### ⏱️ 시간 복잡도

시점 수 N에 대해 각 인덱스는 한 번 들어가고 최대 한 번 나옵니다. 전체 while 실행 횟수도 O(N)이라 시간은 O(N)입니다.

### 💾 공간 복잡도

인덱스 스택과 반환 리스트에 추가 공간 O(N)을 씁니다.

## ⚠️ 실수하기 쉬운 점

- 가격이 같으면 떨어진 것이 아닙니다.
- 마지막 시점에서 기다릴 수 있는 시간은 0입니다.

## ✅ 배운 것

결과를 아직 모르는 시점을 스택에 두고 답이 확정되는 순간 꺼내 기록합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 가격이 계속 오르는 경우와 계속 내려가는 경우를 추적하기

## 🚀 이어 풀어 볼 문제

- [짝지어 제거하기](https://school.programmers.co.kr/learn/courses/30/lessons/12973) (`12973`) — 각 항목이 최대 한 번 들어가고 나오는 스택을 복습합니다.
- [프로세스](https://school.programmers.co.kr/learn/courses/30/lessons/42587) (`42587`) — 아직 처리되지 않은 항목을 기억하는 방법을 비교합니다.
