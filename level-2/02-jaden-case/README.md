# 🧩 JadenCase 문자열 만들기

- Programmers ID: 12951
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/12951
- Level: 2
- Stage: Level 2 Core 02
- Prerequisites: 01 최댓값과 최솟값, 문자열 메서드
- Core concepts: 공백 보존, capitalize()

## 🎯 이 문제에서 배우는 것

단어를 바꾸면서 원래 공백의 개수도 보존합니다.

## 🔎 문제 핵심

s의 각 단어에서 첫 글자는 대문자로, 뒤의 알파벳은 소문자로 바꿉니다. 숫자로 시작한 단어는 숫자를 그대로 두고 나머지를 소문자로 바꿉니다.

## 💭 먼저 생각해 보기

"  hELLO  2WORLD "에서 공백도 칸으로 그려 보세요. 바꿔야 할 칸과 남겨야 할 칸은 무엇인가요?

## 🧪 예제 이해하기

"  hELLO  2WORLD "의 결과는 "  Hello  2world "입니다. 두 개씩 이어진 공백과 앞뒤 공백이 그대로 남습니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

공백 한 글자를 구분자로 지정해서 나눕니다. 각 조각에 capitalize()를 적용하고 공백 한 글자로 다시 연결합니다.

### 🐍 Python 코드

```python
def solution(s):
    converted = []
    for word in s.split(" "):
        converted.append(word.capitalize())
    return " ".join(converted)
```

### 📖 코드 해설

s.split(" ")은 연속 공백 사이에 빈 문자열도 남깁니다. capitalize()는 첫 문자만 대문자로, 나머지는 소문자로 바꾸며 빈 문자열에도 쓸 수 있습니다. " ".join()으로 빈 조각까지 연결하므로 공백 개수를 지킵니다. split()처럼 구분자를 생략하면 연속 공백이 합쳐집니다.

### ⏱️ 시간 복잡도

문자열 길이를 N이라 하면 분리·대소문자 변환·연결에 각각 O(N)이 들어 전체 O(N)입니다.

### 💾 공간 복잡도

조각 리스트와 변환 문자열, 반환 문자열을 포함해 추가 공간은 O(N)입니다.

## ⚠️ 실수하기 쉬운 점

- title()은 숫자 뒤의 알파벳까지 대문자로 만들 수 있어 이 규칙과 다릅니다.
- 원래 문자열을 strip()으로 다듬으면 앞뒤 공백을 잃습니다.

## ✅ 배운 것

구분자를 지정해 빈 조각까지 남기면 공백을 보존하며 단어를 바꿀 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 연속 공백과 숫자로 시작하는 단어를 함께 확인하기

## 🚀 이어 풀어 볼 문제

- [최댓값과 최솟값](https://school.programmers.co.kr/learn/courses/30/lessons/12939) (`12939`) — 문자열을 나누는 방법을 복습합니다.
- [튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065) (`64065`) — 구분자를 보고 문자열 속 자료를 읽습니다.
