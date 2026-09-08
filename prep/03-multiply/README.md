# 🧩 두 수의 곱 구하기

- Programmers ID: 120804
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/120804
- Level: 0
- Stage: Python Prep 03
- Prerequisites: 정수, 함수, 매개변수, `return`
- Core concepts: 곱셈 연산자 `*`

## 🎯 이 문제에서 배우는 것

Python에서 곱셈을 쓰는 방법을 배웁니다. 수학에서는 곱셈 기호로 `×`를 쓰지만 Python 코드에서는 `*`를 씁니다.

## 🔎 문제 핵심

정수 `num1`과 `num2`를 곱한 값을 반환합니다.

## 💭 먼저 생각해 보기

1. Python의 곱셈 기호는 무엇인가요?
2. 계산 결과를 어느 변수에 담을까요?
3. 값을 돌려주는 명령은 무엇인가요?

## 🧪 예제 이해하기

`num1`이 6이고 `num2`가 7이라면 `6 * 7`을 계산합니다. 결과는 42입니다.

## 🛠️ 풀이 1. 두 수 곱하기

### 💡 아이디어

곱셈 연산자 `*`를 사용해 두 매개변수를 곱합니다.

### 🐍 Python 코드

```python
def solution(num1, num2):
    answer = num1 * num2
    return answer
```

### 📖 코드 해설

`num1 * num2`가 두 수의 곱을 계산합니다. 계산 결과는 `answer`에 저장되고 `return answer`로 함수 밖에 전달됩니다.

### ⏱️ 시간 복잡도

곱셈을 한 번 하므로 `O(1)`입니다.

### 💾 공간 복잡도

결과 변수 하나를 사용하므로 `O(1)`입니다.

## ⚠️ 실수하기 쉬운 점

- 코드에 `×`를 입력하면 Python이 곱셈으로 알아듣지 못합니다.
- `num1 ** num2`는 곱셈이 아니라 거듭제곱입니다.

## ✅ 배운 것

- Python의 곱셈 연산자는 `*`입니다.
- 계산한 값은 변수에 저장한 뒤 반환합니다.

## 🔁 다시 풀어보기

- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법을 말로 설명하기

## 🚀 이어 풀어 볼 문제

- [편지](https://school.programmers.co.kr/learn/courses/30/lessons/120898) (`120898`) — 글자 수와 한 글자의 너비를 곱해 전체 길이를 구합니다.
- [세균 증식](https://school.programmers.co.kr/learn/courses/30/lessons/120910) (`120910`) — 같은 수를 거듭 곱했을 때 값이 어떻게 커지는지 살펴봅니다.
