# 🧩 나누어 떨어지는 숫자 배열

- Programmers ID: 12910
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/12910
- Level: 1
- Stage: Level 1 Core 18
- Prerequisites: `%`, 조건문, 리스트, `sorted()`
- Core concepts: 조건으로 고르기, 정렬, 예외 결과

## 🎯 이 문제에서 배우는 것

값을 고르는 조건과 결과를 나열하는 순서를 각각 처리합니다.

## 🔎 문제 핵심

리스트 `arr`에서 `divisor`로 나누어 떨어지는 값들을 작은 순서로 돌려줍니다. 하나도 없으면 `[-1]`을 돌려줍니다.

## 💭 먼저 생각해 보기

`[14, 3, 8, 5]`에서 2로 나누어 떨어지는 수를 먼저 표시해 보세요. 표시한 수를 어떤 순서로 돌려줘야 할까요?

## 🧪 예제 이해하기

`arr = [14, 3, 8, 5]`, `divisor = 2`이면 14와 8을 고릅니다. 작은 순서로 놓은 결과는 `[8, 14]`입니다. 같은 리스트를 9로 검사하면 `[-1]`입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

나머지가 0인 값을 새 리스트에 담습니다. 빈 리스트이면 특수 결과를 돌려주고 값이 있으면 정렬합니다.

### 🐍 Python 코드

```python
def solution(arr, divisor):
    divisible = []
    for number in arr:
        if number % divisor == 0:
            divisible.append(number)

    if len(divisible) == 0:
        return [-1]
    return sorted(divisible)
```

### 📖 코드 해설

`divisible`에는 조건에 맞는 값만 들어갑니다. `sorted(divisible)`은 정렬한 새 리스트를 돌려줍니다. 입력 `arr`도, 고른 값을 담은 `divisible`도 정렬 과정에서 직접 바꾸지 않습니다.

### ⏱️ 시간 복잡도

입력 원소 수를 `n`, 고른 원소 수를 `k`라고 하면 검사에 `O(n)`, 정렬에 최악 `O(k log k)`가 듭니다. 전체는 `O(n + k log k)`입니다. `k`가 0이나 1이면 정렬 작업은 일정한 크기입니다.

### 💾 공간 복잡도

고른 리스트와 정렬된 반환 리스트, 정렬 도중의 임시 공간이 필요합니다. 반환값을 포함해 `O(k + 1)`이며 `+ 1`은 고른 값이 없을 때의 `[-1]`도 포함합니다.

## ⚠️ 실수하기 쉬운 점

- 조건에 맞는 값을 찾았다고 바로 하나만 반환하면 안 됩니다.
- 빈 결과는 정수 -1이 아니라 리스트 `[-1]`입니다.
- `divisible.sort()`는 리스트를 직접 바꾸고 `None`을 반환하므로 `return divisible.sort()`라고 쓰지 않습니다.

## ✅ 배운 것

고르기와 정렬은 서로 다른 작업이며 두 작업의 비용을 함께 세어야 합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법을 말로 설명하기
- [ ] divisor가 1일 때 모든 값이 결과에 남는 이유 설명하기

## 🚀 이어 풀어 볼 문제

- [약수의 합](https://school.programmers.co.kr/learn/courses/30/lessons/12928) (`12928`) — 나누어 떨어지는 관계를 약수와 연결합니다.
- [제일 작은 수 제거하기](https://school.programmers.co.kr/learn/courses/30/lessons/12935) (`12935`) — 원래 순서를 지키며 값을 고르는 경우와 비교합니다.
