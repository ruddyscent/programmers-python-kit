# 🧩 소수 찾기

- Programmers ID: 42839
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42839
- Level: 2
- Stage: Level 2 Core 22
- Prerequisites: 21 순열, 집합, 약수 판별
- Core concepts: 여러 길이의 후보, 소수 검사

## 🎯 이 문제에서 배우는 것

후보를 만드는 작업과 조건을 검사하는 작업을 나눕니다.

## 🔎 문제 핵심

numbers의 한 자리 숫자 조각을 일부 또는 전부 사용해 만들 수 있는 서로 다른 소수의 개수를 돌려줍니다. 각 조각은 한 후보에서 한 번만 쓸 수 있습니다.

## 💭 먼저 생각해 보기

"23"의 한 장짜리와 두 장짜리 수를 모두 적어 보세요. 같은 수가 여러 순서에서 나올 때 여러 번 셀까요?

## 🧪 예제 이해하기

"23"으로 만든 수는 2, 3, 23, 32입니다. 앞의 세 수가 소수라 답은 3입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

길이 1부터 전체 길이까지 순열을 만들고 정수로 바꿔 집합에 넣습니다. 각 후보가 2 이상이고 제곱근 이하에 약수가 없는지 확인합니다.

### 🐍 Python 코드

```python
from itertools import permutations
from math import isqrt


def solution(numbers):
    candidates = set()
    for length in range(1, len(numbers) + 1):
        for digits in permutations(numbers, length):
            candidates.add(int("".join(digits)))

    count = 0
    for candidate in candidates:
        if candidate < 2:
            continue
        is_prime = True
        for divisor in range(2, isqrt(candidate) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count
```

### 📖 코드 해설

permutations(numbers, length)는 지정한 개수의 조각으로 만든 순서입니다. 숫자 0이 앞에 붙은 표현도 int()로 바꾸면 같은 정수가 됩니다. 소수는 1과 자기 자신만 양의 약수인 2 이상의 수입니다. 합성수는 곱의 작은 쪽 약수가 제곱근 이하에 있으므로 거기까지만 확인해도 됩니다. continue는 현재 반복의 나머지를 건너뛰고 다음 후보로 이동합니다.

### ⏱️ 시간 복잡도

조각 수 N, 중복 제거 후 후보 수 U, 최대 후보값 V라 하면 생성에 O(N × N!), 판별에 최악 O(U × sqrt(V))가 듭니다. 전체는 두 비용의 합입니다. N은 최대 7입니다.

### 💾 공간 복잡도

후보 집합 U개와 현재 순열·문자열 N칸을 저장합니다. 반환값을 포함해 추가 공간은 O(U + N)입니다.

## ⚠️ 실수하기 쉬운 점

- 0과 1은 소수가 아닙니다.
- 같은 숫자 조각이나 앞의 0 때문에 생긴 같은 정수를 중복으로 세지 않습니다.

## ✅ 배운 것

후보 생성과 소수 검사를 나누고 같은 수는 집합으로 한 번만 셉니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 0이 들어간 입력과 같은 숫자 조각이 여러 개인 입력 확인하기

## 🚀 이어 풀어 볼 문제

- [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) (`87946`) — 순서가 다른 후보들을 생성하는 방법을 복습합니다.
- [카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842) (`42842`) — 제곱근 이하의 약수 후보를 살펴봅니다.
