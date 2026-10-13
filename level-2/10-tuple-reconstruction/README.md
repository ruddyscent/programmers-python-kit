# 🧩 튜플

- Programmers ID: 64065
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/64065
- Level: 2
- Stage: Level 2 Core 10
- Prerequisites: 01 split(), 집합, 정렬 기준
- Core concepts: 문자열 해석, 집합의 크기

## 🎯 이 문제에서 배우는 것

순서가 섞인 집합들의 관계에서 원래 순서를 복원합니다.

## 🔎 문제 핵심

s는 튜플의 첫 원소, 첫 두 원소, 첫 세 원소 등을 집합으로 적은 문자열입니다. 집합과 집합 안의 원소 순서는 섞일 수 있습니다. 원래 튜플의 순서를 리스트로 돌려줍니다.

## 💭 먼저 생각해 보기

한 장에는 7, 다른 장에는 4와 7이 적혀 있습니다. 세 번째 장에 9, 7, 4가 적혀 있다면 매번 새로 늘어난 숫자는 무엇인가요?

## 🧪 예제 이해하기

"{{9,7,4},{7},{4,7}}"를 크기순으로 읽으면 {7}, {4,7}, {9,7,4}입니다. 새로 나온 값이 7, 4, 9라 결과는 [7, 4, 9]입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

바깥 괄호를 제외한 문자열을 집합별로 나눠 정수 리스트로 바꿉니다. 원소 개수로 정렬하고 아직 보지 못한 값을 순서대로 담습니다.

### 🐍 Python 코드

```python
def solution(s):
    groups = []
    for chunk in s[2:-2].split("},{"):
        group = []
        for token in chunk.split(","):
            group.append(int(token))
        groups.append(group)

    seen = set()
    result = []
    for group in sorted(groups, key=len):
        for number in group:
            if number not in seen:
                seen.add(number)
                result.append(number)
    return result
```

### 📖 코드 해설

각 원소를 groups에 담은 뒤 key=len으로 원소 개수가 적은 그룹부터 정렬합니다. 올바른 입력에서는 다음 그룹에 새 값이 꼭 하나 늘어납니다. 문자열 길이로 정렬하면 여러 자리 숫자 때문에 순서가 달라질 수 있어 정수로 읽은 리스트의 길이를 씁니다. 실제 Python 튜플을 반환하는 문제가 아니라 원소 리스트를 반환합니다.

### ⏱️ 시간 복잡도

문자열 길이를 M, 집합 개수를 K라 하면 해석과 전체 원소 확인에 O(M), 그룹 정렬에 O(K log K)가 듭니다. 정수와 집합 연산의 문제 범위 비용을 포함해 평균 O(M + K log K)입니다.

### 💾 공간 복잡도

분리한 문자열, 그룹 리스트, 집합과 반환 리스트를 포함해 추가 공간은 O(M + K)입니다.

## ⚠️ 실수하기 쉬운 점

- 숫자의 크기로 정렬하는 문제가 아닙니다.
- 쉼표 전체를 한 번에 나누면 어느 집합의 값인지 잃습니다.

## ✅ 배운 것

그룹이 커질 때 하나씩 새로 늘어나는 원소가 원래의 순서를 알려 줍니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 집합 내부 순서와 집합 나열 순서를 바꿔도 결과가 같은지 확인하기

## 🚀 이어 풀어 볼 문제

- [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577) (`42577`) — 슬라이싱으로 필요한 문자열 부분을 읽습니다.
- [연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701) (`131701`) — 중복 결과를 집합에 모으는 방법을 연습합니다.
