# 🧩 연속 부분 수열 합의 개수

- Programmers ID: 131701
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/131701
- Level: 2
- Stage: Level 2 Core 30
- Prerequisites: 04 연속 구간, 집합, 누적합
- Core concepts: 원형 수열, 누적합 배열

## 🎯 이 문제에서 배우는 것

구간마다 전체를 다시 더하지 않고 앞에서부터 쌓은 합의 차를 사용합니다.

## 🔎 문제 핵심

끝과 처음이 이어진 elements에서 길이 1부터 전체 길이까지의 연속 구간 합을 구합니다. 서로 다른 합의 개수를 돌려줍니다.

## 💭 먼저 생각해 보기

[1, 2, 3]을 두 번 적고 끝의 3 다음에 1을 이어 읽어 보세요. 구간의 길이를 원래 길이보다 길게 잡아도 될까요?

## 🧪 예제 이해하기

[1, 2, 3]의 길이 1 합은 1,2,3이고 길이 2 합은 3,5,4입니다. 길이 3 합은 6입니다. 서로 다른 값은 1부터 6까지라 답은 6입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

수열을 두 번 이어 적고 맨 앞부터의 합을 prefix에 저장합니다. 구간 합은 끝의 누적합에서 시작 전의 누적합을 빼 구합니다. 모든 시작점과 길이의 합을 집합에 넣습니다.

### 🐍 Python 코드

```python
def solution(elements):
    size = len(elements)
    doubled = elements + elements
    prefix = [0]
    for number in doubled:
        prefix.append(prefix[-1] + number)

    sums = set()
    for start in range(size):
        for length in range(1, size + 1):
            total = prefix[start + length] - prefix[start]
            sums.add(total)
    return len(sums)
```

### 📖 코드 해설

prefix[i]는 맨 앞의 i개 원소 합입니다. 첫 값 0을 넣으면 시작점이 0인 구간도 같은 식을 씁니다. 두 번 이어 놓아 원래 끝을 넘는 구간도 한 줄에서 읽습니다. 시작점은 원래 위치들만, 길이는 원래 수열 길이까지만 확인합니다.

```text
값:       1 2 3 1 2 3
prefix: 0 1 3 6 7 9 12
구간 [1:3]의 합 = prefix[3] - prefix[1] = 5
```

### ⏱️ 시간 복잡도

원소 수 N에 대해 누적합 작성 O(N), 시작점 N개와 길이 N개의 검사 O(N²)입니다. 집합 연산을 평균 O(1)로 세면 전체 평균 O(N²)입니다.

### 💾 공간 복잡도

복사한 수열과 누적합 O(N), 서로 다른 합 U개를 저장하는 집합 O(U)이 필요합니다. 반환값 포함 추가 공간은 O(N + U)이며 U는 최대 N²입니다.

## ⚠️ 실수하기 쉬운 점

- 매 구간에 sum(doubled[start:end])를 쓰면 복사와 덧셈을 반복합니다.
- 같은 합이 여러 위치에서 나와도 한 번만 셉니다.

## ✅ 배운 것

누적합의 차로 각 구간 합을 바로 구하고 집합에 서로 다른 결과만 남깁니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 끝을 넘어가는 구간과 전체 길이 구간을 각각 설명하기

## 🚀 이어 풀어 볼 문제

- [숫자의 표현](https://school.programmers.co.kr/learn/courses/30/lessons/12924) (`12924`) — 합이 목표와 같은 구간을 찾는 방법과 비교합니다.
- [튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065) (`64065`) — 집합으로 중복을 지우는 과정을 복습합니다.
