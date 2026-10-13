# 🧩 카펫

- Programmers ID: 42842
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42842
- Level: 2
- Stage: Level 2 Core 20
- Prerequisites: 약수, 곱셈, Level 1 정수 제곱근
- Core concepts: 후보 크기 탐색, 조건 결합

## 🎯 이 문제에서 배우는 것

넓이가 맞는 후보에서 내부 넓이까지 확인합니다.

## 🔎 문제 핵심

갈색 테두리 한 줄과 노란 내부의 칸 수 brown, yellow가 주어집니다. 가로가 세로 이상인 전체 크기 [가로, 세로]를 돌려줍니다.

## 💭 먼저 생각해 보기

가로 5칸, 세로 3칸 직사각형에서 바깥 한 줄을 빼면 안쪽은 가로·세로 몇 칸인가요?

## 🧪 예제 이해하기

brown = 12, yellow = 3이면 전체 15칸이고 5×3 크기입니다. 내부는 (5-2)×(3-2) = 3칸이라 결과는 [5, 3]입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

전체 칸 수의 약수를 세로 후보로 둡니다. 가로는 전체를 세로로 나눈 몫입니다. 내부가 yellow와 같으면 답을 찾았습니다.

### 🐍 Python 코드

```python
from math import isqrt


def solution(brown, yellow):
    total = brown + yellow
    for height in range(3, isqrt(total) + 1):
        if total % height == 0:
            width = total // height
            if (width - 2) * (height - 2) == yellow:
                return [width, height]
```

### 📖 코드 해설

안쪽 노란 칸이 있으므로 세로는 최소 3입니다. 가로가 세로 이상이어서 세로는 전체 넓이의 제곱근 이하입니다. 양 끝 테두리 두 칸을 빼면 내부 넓이를 구할 수 있습니다. 전체 넓이만 같아서는 테두리 조건을 확인할 수 없습니다.

### ⏱️ 시간 복잡도

전체 칸 수를 T = brown + yellow라 하면 세로 후보를 약 sqrt(T)개 확인하므로 O(sqrt(T))입니다.

### 💾 공간 복잡도

후보와 길이 2인 반환 리스트만 저장합니다. 추가 공간은 반환값 포함 O(1)입니다.

## ⚠️ 실수하기 쉬운 점

- 세로와 가로의 반환 순서를 뒤집지 않습니다.
- 안쪽 넓이에서 한 칸이 아니라 양 끝의 두 칸을 뺍니다.

## ✅ 배운 것

후보의 전체 넓이와 내부 넓이를 모두 검사해 필요한 조건을 빠뜨리지 않습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 정사각형과 노란 내부가 한 칸인 경우 설명하기

## 🚀 이어 풀어 볼 문제

- [N개의 최소공배수](https://school.programmers.co.kr/learn/courses/30/lessons/12953) (`12953`) — 나누어 떨어지는 성질을 복습합니다.
- [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) (`87946`) — 조건에 맞는 후보를 빠짐없이 확인합니다.
