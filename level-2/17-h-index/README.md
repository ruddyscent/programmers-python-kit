# 🧩 H-Index

- Programmers ID: 42747
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42747
- Level: 2
- Stage: Level 2 Core 17
- Prerequisites: 정렬, 조건문, 인덱싱
- Core concepts: 조건을 만족하는 최대 기준

## 🎯 이 문제에서 배우는 것

주어진 수가 아닌 새로운 기준값도 답 후보가 될 수 있음을 익힙니다.

## 🔎 문제 핵심

인용 수 citations에서 h번 이상 인용된 논문이 h편 이상이 되는 h의 최댓값을 돌려줍니다. 기준 h는 논문 수를 넘을 수 없습니다.

## 💭 먼저 생각해 보기

인용 수 [4, 4, 1]에서 기준을 1, 2, 3으로 바꾸며 몇 편이 기준을 넘는지 세어 보세요.

## 🧪 예제 이해하기

[4, 4, 1]은 2번 이상 인용된 논문이 두 편입니다. 3번 이상인 논문은 두 편뿐이라 답은 2입니다. 입력에 2가 없더라도 답이 될 수 있습니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

인용 수를 큰 순서로 정렬합니다. 첫 count편의 마지막 인용 수가 count 이상이면 해당 count를 답으로 갱신합니다.

### 🐍 Python 코드

```python
def solution(citations):
    ordered = sorted(citations, reverse=True)
    best = 0
    for index in range(len(ordered)):
        count = index + 1
        if ordered[index] >= count:
            best = count
        else:
            break
    return best
```

### 📖 코드 해설

큰 순서의 count번째 값이 count 이상이면 앞의 count개 값도 모두 count 이상입니다. 한 번 실패하면 뒤의 값은 더 작고 요구하는 편수는 더 커져 이후도 실패합니다. 구한 최댓값보다 많은 편이 그보다 크게 인용됐다면 더 큰 h도 가능했을 것입니다. 그러므로 최대 기준은 나머지 논문의 조건과도 맞습니다.

### ⏱️ 시간 복잡도

논문 수 N에 대해 정렬 O(N log N), 확인 O(N)이라 전체 O(N log N)입니다.

### 💾 공간 복잡도

정렬된 복사본과 정렬용 임시 공간에 추가 공간 O(N)을 씁니다. 반환값 포함이며 입력은 보존합니다.

## ⚠️ 실수하기 쉬운 점

- h를 인용 수 중에서만 고르면 답을 놓칩니다.
- 모든 인용 수가 0이면 답은 0입니다.

## ✅ 배운 것

입력 값에 없는 수라도 문제의 조건을 만족하는 기준값이면 답이 될 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 답이 입력 원소에 없는 경우와 전부 0인 경우 설명하기

## 🚀 이어 풀어 볼 문제

- [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746) (`42746`) — 어떤 값으로 정렬할지 다시 생각합니다.
- [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) (`42885`) — 정렬 뒤 양 끝에서 조건을 확인합니다.
