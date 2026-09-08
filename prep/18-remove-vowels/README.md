# 모음 제거

- Programmers ID: 120849
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/120849
- Level: 0
- Stage: Python Prep 18
- Prerequisites: 문자열, `for`, `if`, `in`과 `not in`
- Core concepts: 여러 문자 중 하나인지 확인하기, 필요한 문자만 골라 담기
- Status: 학습 자료 준비됨 (Programmers 채점 미확인)

## 이 문제에서 배우는 것

`in`은 어떤 값이 모음 안에 들어 있는지 확인할 때도 씁니다. `not in`을 사용하면 모음이 아닌 글자만 골라 새 문자열에 담습니다.

## 문제 핵심

영어 소문자 모음은 `a`, `e`, `i`, `o`, `u`입니다. 이 다섯 글자를 `"aeiou"`에 모아 두고 현재 글자가 그 안에 없는 경우만 결과에 붙입니다.

## 먼저 생각해 보기

`"apple pie"`를 왼쪽부터 살펴보세요. 모음에는 줄을 긋고 남은 자음과 공백을 순서대로 읽어 봅니다.

## 예제 이해하기

`"apple pie"`에서 `a`, `e`, `i`, `e`를 빼면 `"ppl p"`가 남습니다. 공백은 모음이 아니므로 결과에도 그대로 남아 있습니다.

## 풀이 1. 이해하기 쉬운 방법

### 아이디어

1. 다섯 모음을 `vowels`에 저장합니다.
2. 원래 문자열의 글자를 하나씩 확인합니다.
3. 글자가 `vowels` 안에 없을 때만 결과에 붙입니다.
4. 완성한 문자열을 돌려줍니다.

### Python 코드

```python
def solution(my_string):
    vowels = "aeiou"
    answer = ""

    for character in my_string:
        if character not in vowels:
            answer += character

    return answer
```

### 코드 해설

`character not in vowels`는 현재 글자가 `"aeiou"` 안에 없으면 참입니다. 자음과 공백은 이 조건을 통과해 `answer`에 들어갑니다. 모음은 조건을 통과하지 못하므로 자연스럽게 빠집니다.

### 반복 횟수와 저장 공간

문자열 길이가 `n`이라면 글자를 `n`번 확인합니다. 새 문자열에는 모음을 뺀 나머지 글자가 저장됩니다.

## 실수하기 쉬운 점

- 모음은 `a`, `e`, `i`, `o`, `u` 다섯 개입니다.
- 공백은 지우지 않습니다.
- 이 문제의 입력에는 영어 소문자와 공백만 들어옵니다.

## 배운 것

- `in`은 값이 문자열 안에 있는지 확인합니다.
- `not in`은 값이 문자열 안에 없는지 확인합니다.
- 제거할 글자가 여러 개여도 남길 글자만 모읍니다.

## 다시 풀어보기

- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법을 말로 설명하기
- [ ] 모음만 있는 문자열을 넣으면 어떤 결과가 나오는지 생각하기
