# 🧩 의상

- Programmers ID: 42578
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42578
- Level: 2
- Stage: Level 2 Core 09
- Prerequisites: 리스트 순회, 곱셈, 튜플 언패킹
- Core concepts: 딕셔너리, 종류별 선택 수

## 🎯 이 문제에서 배우는 것

종류마다 선택할 수 있는 수를 세고 조합의 수를 곱합니다.

## 🔎 문제 핵심

clothes의 각 항목은 [이름, 종류]입니다. 같은 종류는 최대 하나만 입고 적어도 한 개는 입을 때 가능한 옷차림 수를 돌려줍니다.

## 💭 먼저 생각해 보기

모자 두 개와 신발 한 켤레가 있습니다. 각 종류를 안 쓰는 선택까지 적고 아무것도 안 입은 경우를 마지막에 찾아보세요.

## 🧪 예제 이해하기

모자 종류에 2개, 신발 종류에 1개라면 선택 수는 각각 3과 2입니다. 3×2에서 아무것도 안 입는 한 경우를 빼 결과는 5입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

종류를 이름표로 삼아 개수를 저장합니다. 각 종류의 개수에 안 입는 선택 1을 더해 모두 곱하고 마지막에 1을 뺍니다.

### 🐍 Python 코드

```python
def solution(clothes):
    category_counts = {}
    for name, category in clothes:
        category_counts[category] = category_counts.get(category, 0) + 1

    combinations = 1
    for count in category_counts.values():
        combinations *= count + 1
    return combinations - 1
```

### 📖 코드 해설

{}는 빈 딕셔너리입니다. 딕셔너리는 키와 값을 짝지어 저장하며 여기서는 종류가 키, 개수가 값입니다. get(category, 0)은 키가 아직 없으면 0을 읽습니다. values()는 저장된 개수들을 꺼냅니다. 종류 하나를 골라도 다른 종류의 선택은 제한되지 않아 선택 수를 곱할 수 있습니다.

### ⏱️ 시간 복잡도

옷 수를 N, 종류 문자열의 최대 길이를 L이라 하면 해시 계산과 종류별 순회에 평균 O(NL)이 듭니다. 문제 범위의 정수 곱셈을 한 번의 연산으로 셉니다.

### 💾 공간 복잡도

종류 수 C만큼 딕셔너리 항목을 만듭니다. 기존 문자열을 키로 사용하며 반환값을 포함한 추가 공간은 O(C)입니다.

## ⚠️ 실수하기 쉬운 점

- 종류별 개수를 더하면 함께 입는 조합을 놓칩니다.
- 아무것도 안 입는 경우는 전체에서 한 번만 뺍니다.

## ✅ 배운 것

딕셔너리로 종류별 개수를 세고 서로 독립인 선택 수를 곱합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 종류 하나만 있을 때와 각 옷의 종류가 모두 다를 때 설명하기

## 🚀 이어 풀어 볼 문제

- [영어 끝말잇기](https://school.programmers.co.kr/learn/courses/30/lessons/12981) (`12981`) — 값의 존재 기록과 개수 기록을 비교합니다.
- [튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065) (`64065`) — 종류와 등장 순서를 구별하는 연습을 합니다.
