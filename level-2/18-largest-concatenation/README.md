# 🧩 가장 큰 수

- Programmers ID: 42746
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42746
- Level: 2
- Stage: Level 2 Core 18
- Prerequisites: 정렬 기준 함수, 문자열 연결
- Core concepts: 두 값의 상대 순서, cmp_to_key()

## 🎯 이 문제에서 배우는 것

숫자의 크기 대신 연결했을 때의 크기를 비교합니다.

## 🔎 문제 핵심

numbers를 순서만 바꾸어 이어 붙였을 때 만들 수 있는 가장 큰 수를 문자열로 돌려줍니다. 모든 값이 0이면 "0"입니다.

## 💭 먼저 생각해 보기

12와 121을 어느 순서로 붙여야 클까요? 두 결과를 모두 적고 왼쪽부터 비교하세요.

## 🧪 예제 이해하기

[12, 121]은 "12121"과 "12112" 중 앞의 값이 더 큽니다. 따라서 12를 먼저 둡니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

두 문자열 first, second의 연결 결과를 비교하는 함수를 만듭니다. 더 큰 연결을 만드는 순서가 앞에 오도록 정렬하고 붙입니다.

### 🐍 Python 코드

```python
from functools import cmp_to_key


def solution(numbers):
    parts = []
    for number in numbers:
        parts.append(str(number))

    def compare(first, second):
        if first + second > second + first:
            return -1
        if first + second < second + first:
            return 1
        return 0

    parts.sort(key=cmp_to_key(compare))
    if parts[0] == "0":
        return "0"
    return "".join(parts)
```

### 📖 코드 해설

비교 함수는 첫 값이 먼저 와야 하면 음수, 나중이면 양수, 순서가 같아도 되면 0을 돌려줍니다. cmp_to_key()는 이 비교를 sorted()나 sort()의 기준으로 사용할 수 있게 합니다. 두 값을 바꿔 붙여도 전체 자릿수는 같으므로 문자열로 크기를 비교할 수 있습니다. 이웃한 두 값을 이 규칙에 맞게 바꾸면 전체 연결값도 작아지지 않습니다. parts는 새 리스트라 원래 numbers를 바꾸지 않습니다.

### ⏱️ 시간 복잡도

수의 개수를 N, 최대 자릿수를 L이라 하면 비교할 때 문자열 연결과 비교가 O(L), 전체 정렬은 O(N log N × L)입니다. 연결하는 O(NL)도 포함하며 이 문제에서 L은 최대 4입니다.

### 💾 공간 복잡도

숫자 문자열, 정렬용 임시 공간, 반환 문자열을 포함해 추가 공간은 O(NL)입니다.

## ⚠️ 실수하기 쉬운 점

- 정수 내림차순만으로 정렬하면 12와 121의 순서를 틀립니다.
- 긴 최종 문자열을 int()로 바꿀 필요는 없습니다. 모든 0은 첫 글자로 확인합니다.

## ✅ 배운 것

정렬할 두 항목을 바꿔 보며 최종 결과에 유리한 상대 순서를 정할 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 접두어가 비슷한 수와 모든 값이 0인 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747) (`42747`) — 정렬 기준과 최종 답 후보를 구별합니다.
- [JadenCase 문자열 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12951) (`12951`) — 문자열 조각을 join()으로 연결합니다.
