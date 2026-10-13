# 🧩 땅따먹기

- Programmers ID: 12913
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/12913
- Level: 2
- Stage: Level 2 Core 28
- Prerequisites: 27 동적 계획법, 2차원 리스트
- Core concepts: 마지막 열을 상태로 기억

## 🎯 이 문제에서 배우는 것

현재 최고 점수 하나로는 부족할 때 필요한 조건별로 답을 나눠 저장합니다.

## 🔎 문제 핵심

land의 각 행에서 네 칸 중 하나를 선택하며 내려옵니다. 연속된 두 행에서 같은 열을 고를 수 없을 때 점수 합의 최댓값을 돌려줍니다.

## 💭 먼저 생각해 보기

첫 행 [9, 8, 1, 1], 다음 행 [9, 1, 1, 1]에서 첫 행의 9부터 고르면 최선인가요?

## 🧪 예제 이해하기

첫 행의 두 번째 값 8과 다음 행의 첫 값 9를 고르면 17점입니다. 첫 행의 최댓값 9를 고르면 다음에는 최대 1만 더해 10점이라 답을 놓칩니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

이전 행에서 각 열로 끝난 최고 점수 네 개를 저장합니다. 다음 행의 한 열에서는 그 열을 제외한 이전 세 답 중 최댓값을 더합니다.

### 🐍 Python 코드

```python
def solution(land):
    previous = land[0][:]
    for row in range(1, len(land)):
        current = [0] * 4
        for column in range(4):
            best_before = 0
            for last_column in range(4):
                if last_column != column:
                    best_before = max(best_before, previous[last_column])
            current[column] = land[row][column] + best_before
        previous = current
    return max(previous)
```

### 📖 코드 해설

previous[column]은 그 열에서 끝났을 때의 최댓값입니다. 같은 열에서 끝난 값은 후보에서 제외합니다. 현재 열만 알면 다음 행에서 금지할 열을 알 수 있습니다. 그래서 더 오래전의 경로를 저장할 필요가 없습니다. current를 따로 만들어 한 행을 계산하는 중 이전 답을 덮어쓰지 않습니다. 첫 행도 복사해 입력을 보존합니다.

### ⏱️ 시간 복잡도

행 수 R에 대해 행마다 4×4번 확인합니다. 열 수가 4로 고정되어 시간은 O(R)입니다.

### 💾 공간 복잡도

이전과 현재 네 값씩만 유지합니다. 반환값을 포함한 추가 공간은 O(1)입니다.

## ⚠️ 실수하기 쉬운 점

- 행마다 가장 큰 값을 바로 고르는 그리디는 앞 예처럼 실패합니다.
- 현재 행을 계산하는 도중 previous의 일부만 바꾸면 서로 다른 행의 답이 섞입니다.

## ✅ 배운 것

다음 선택에 영향을 주는 마지막 열을 상태로 기억하면 그보다 오래된 경로를 모두 보관할 필요가 없습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 최고 점수 하나가 아니라 열별 네 답이 필요한 이유 설명하기

## 🚀 이어 풀어 볼 문제

- [멀리 뛰기](https://school.programmers.co.kr/learn/courses/30/lessons/12914) (`12914`) — 이전 답만 유지하는 DP를 복습합니다.
- [행렬의 곱셈](https://school.programmers.co.kr/learn/courses/30/lessons/12949) (`12949`) — 2차원 좌표로 값을 계산합니다.
