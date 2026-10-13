# 🧩 모음사전

- Programmers ID: 84512
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/84512
- Level: 2
- Stage: Level 2 Core 23
- Prerequisites: 함수, 문자열 연결, 길이 조건
- Core concepts: 재귀 함수, 깊이 우선 생성

## 🎯 이 문제에서 배우는 것

짧은 단어에서 글자 하나를 붙이는 일을 반복해 사전순으로 후보를 만듭니다.

## 🔎 문제 핵심

A, E, I, O, U만으로 만든 길이 1부터 5까지의 단어가 사전순으로 있을 때 word가 몇 번째인지 돌려줍니다. 순서는 1부터 셉니다.

## 💭 먼저 생각해 보기

"A", "AA", "AAA"처럼 늘려 적어 보세요. 긴 단어를 만들기 전에 짧은 단어를 기록해야 할까요?

## 🧪 예제 이해하기

길이 5인 단어 AAAAA 다음에는 마지막 글자를 바꾼 AAAAE, AAAAI, AAAAO가 이어집니다. AAAAA가 5번째이므로 word = "AAAAO"의 답은 8입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

현재 단어를 기록하고 A부터 U까지 하나씩 붙여 같은 함수를 호출합니다. 길이가 5이면 더 붙이지 않고 돌아옵니다. 만든 목록에서 word의 위치를 찾습니다.

### 🐍 Python 코드

```python
def solution(word):
    dictionary = []

    def build(prefix):
        if prefix:
            dictionary.append(prefix)
        if len(prefix) == 5:
            return
        for vowel in "AEIOU":
            build(prefix + vowel)

    build("")
    return dictionary.index(word) + 1
```

### 📖 코드 해설

함수가 자기 자신을 부르는 것을 재귀라고 합니다. 호출할 때마다 prefix가 한 글자 길어져 길이 5에서 멈춥니다. 한 갈래를 끝까지 만든 뒤 돌아와 다음 모음을 붙이는 순서는 깊이 우선 탐색(DFS)입니다. 짧은 단어를 먼저 기록하고 모음을 사전순으로 붙여 전체 사전순을 지킵니다. index(word)는 처음 위치를 0부터 세므로 1을 더합니다.

```text
A -> AA -> AAA -> …
     AE -> AEA -> …
E -> EA -> EAA -> …
```

### ⏱️ 시간 복잡도

생성한 단어 수를 W, 최대 길이를 D라 하면 문자열 복사와 검색까지 O(WD)입니다. 현재 문제에서는 D=5, W=5+25+125+625+3125=3905로 고정되어 있습니다.

### 💾 공간 복잡도

단어 목록과 문자열에 O(WD), 재귀 호출 경로에 O(D)을 씁니다. 반환값을 포함한 전체 추가 공간은 O(WD)입니다.

## ⚠️ 실수하기 쉬운 점

- 끝 조건이 없으면 계속 자기 자신을 부르게 됩니다.
- 빈 문자열은 사전의 단어로 세지 않습니다.

## ✅ 배운 것

재귀는 작은 상태를 다음 상태로 확장하고 종료 조건에서 이전 호출로 돌아갑니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 이전 호출로 돌아오는 시점과 다음 모음을 붙이는 시점 설명하기

## 🚀 이어 풀어 볼 문제

- [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) (`43165`) — 한 단계마다 두 선택으로 갈라지는 DFS를 연습합니다.
- [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) (`87946`) — 후보를 모두 살피는 순서와 목적을 비교합니다.
