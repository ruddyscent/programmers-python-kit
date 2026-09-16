# 🧩 음양 더하기

- Programmers ID: 76501
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/76501
- Level: 1
- Stage: Level 1 Core 23
- Prerequisites: 리스트 인덱싱, `range()`, `if`, `True`와 `False`
- Core concepts: 같은 위치의 값 연결, 부호 적용

## 🎯 이 문제에서 배우는 것

두 리스트의 같은 위치를 함께 읽어 하나의 수를 만들고 더합니다.

## 🔎 문제 핵심

`absolutes`에는 부호를 뺀 양의 크기가, `signs`에는 각 수의 부호가 들어 있습니다. 같은 위치의 부호가 `True`이면 양수, `False`이면 음수로 계산한 전체 합을 돌려줍니다.

## 💭 먼저 생각해 보기

크기 `[3, 8, 2]`와 부호 `[True, False, True]`를 위아래로 써 보세요. 같은 위치끼리 연결한 실제 수는 무엇인가요?

## 🧪 예제 이해하기

두 리스트가 `[3, 8, 2]`, `[True, False, True]`이면 실제 수는 3, -8, 2입니다. 합계는 `3 - 8 + 2 = -3`입니다.

```text
위치:       0      1      2
absolutes:  3      8      2
signs:     True  False  True
실제 수:    3     -8      2
```

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

인덱스로 두 리스트를 함께 읽습니다. 부호가 참이면 크기를 더하고 거짓이면 뺍니다.

### 🐍 Python 코드

```python
def solution(absolutes, signs):
    total = 0
    for index in range(len(absolutes)):
        if signs[index]:
            total += absolutes[index]
        else:
            total -= absolutes[index]
    return total
```

### 📖 코드 해설

`if signs[index]:`는 그 위치의 값이 참인지 검사합니다. `total -= value`는 `total = total - value`와 같습니다. 두 리스트의 길이가 같으므로 하나의 인덱스로 함께 읽을 수 있습니다.

### ⏱️ 시간 복잡도

두 리스트의 공통 길이를 `n`이라 하면 각 위치를 한 번씩 확인하므로 시간은 `O(n)`입니다.

### 💾 공간 복잡도

합계와 현재 위치만 저장합니다. 반환값을 포함한 추가 공간은 `O(1)`입니다.

## ✨ 풀이 2. `zip()`으로 같은 위치끼리 묶기

### 💡 아이디어

`zip()`은 여러 자료에서 같은 위치의 값을 하나씩 묶어 줍니다. 크기와 부호를 바로 받아 인덱스 없이 읽습니다.

### 🐍 Python 코드

```python
def solution(absolutes, signs):
    total = 0
    for absolute, is_positive in zip(absolutes, signs):
        if is_positive:
            total += absolute
        else:
            total -= absolute
    return total
```

### 📖 코드 해설

첫 묶음 `(3, True)`를 받으면 3은 `absolute`, `True`는 `is_positive`에 들어갑니다. 묶음의 값을 변수 여러 개에 나누어 받는 것을 언패킹이라고 합니다. `zip()`은 더 짧은 자료가 끝나면 멈춥니다. 이 문제는 두 길이가 같아서 모든 원소가 처리됩니다. 인덱스 대신 값의 이름을 읽을 수 있는 표현입니다.

### ⏱️ 시간 복잡도

공통 길이 `n`에 대해 한 번 순회하므로 `O(n)`입니다.

### 💾 공간 복잡도

`zip()`은 모든 묶음을 리스트로 미리 만들지 않고 하나씩 꺼냅니다. 반환값을 포함한 추가 공간은 `O(1)`입니다.

## ⚠️ 실수하기 쉬운 점

- 부호와 크기의 위치가 대응하므로 한 리스트만 정렬하면 안 됩니다.
- Python에서는 참·거짓을 `True`, `False`로 씁니다. 소문자 `true`, `false`가 아닙니다.

## ✅ 배운 것

같은 인덱스에 의미가 연결된 자료는 순서를 유지한 채 함께 읽어야 합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법을 말로 설명하기
- [ ] 모두 음수인 경우와 합계가 0인 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [내적](https://school.programmers.co.kr/learn/courses/30/lessons/70128) (`70128`) — 두 리스트의 같은 위치끼리 곱하는 문제를 풉니다.
- [평균 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/12944) (`12944`) — 부호를 이미 가진 수들의 합계와 평균을 구합니다.
