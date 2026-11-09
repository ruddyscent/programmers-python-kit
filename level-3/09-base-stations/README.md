# 🧩 기지국 설치

- Programmers ID: 12979
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/12979
- Level: 3
- Stage: Level 3 Core 09
- Prerequisites: 몫 //, 08 그리디 선택
- Core concepts: 빈 구간 길이, 올림 나눗셈

## 🎯 이 문제에서 배우는 것

칸을 하나씩 보지 않고 빈 구간의 길이로 필요한 개수를 계산합니다.

## 🔎 문제 핵심

1번부터 n번까지 아파트가 한 줄로 있고 stations의 아파트에는 이미 기지국이 있습니다. 기지국 하나는 양쪽으로 w칸까지 전파를 보냅니다. 모든 아파트에 전파가 닿도록 추가로 세워야 하는 기지국의 최소 개수를 돌려줍니다.

## 💭 먼저 생각해 보기

w = 1이면 기지국 하나가 몇 칸을 덮나요? 전파가 닿지 않는 칸이 7칸 연속이면 몇 개가 필요할까요?

## 🧪 예제 이해하기

n = 12, stations = [6], w = 1이면 5~7번이 덮입니다. 1~4번은 4칸이라 3칸씩 덮으면 2개, 8~12번은 5칸이라 2개가 필요합니다. 결과는 4입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

기지국 하나가 덮는 길이는 2w + 1입니다. 기존 기지국 사이의 빈 구간마다 길이를 이 값으로 나눠 올림하면 필요한 개수입니다.

### 🐍 Python 코드

```python
def solution(n, stations, w):
    coverage = 2 * w + 1
    added = 0
    first_uncovered = 1
    for station in stations:
        left = station - w
        if first_uncovered < left:
            gap = left - first_uncovered
            added += (gap + coverage - 1) // coverage
        first_uncovered = station + w + 1

    if first_uncovered <= n:
        gap = n - first_uncovered + 1
        added += (gap + coverage - 1) // coverage
    return added
```

### 📖 코드 해설

first_uncovered는 아직 확인하지 않은 칸 가운데 가장 앞 칸입니다. 다음 기지국이 덮기 시작하는 칸 left가 그보다 뒤에 있으면 그 사이가 빈 구간입니다. (gap + coverage - 1) // coverage는 나누어떨어지지 않을 때 몫을 하나 올리는 올림 나눗셈입니다. 예를 들어 gap이 4, coverage가 3이면 6 // 3 = 2입니다. 마지막 기지국 뒤에 남은 칸도 같은 방법으로 셉니다. stations는 오름차순으로 주어집니다.

```text
칸    1 2 3 4 | 5 6 7 | 8 9 10 11 12
빈칸  4칸     | 기존  | 5칸
필요  2개              2개
```

빈 구간을 왼쪽 끝부터 2w + 1칸씩 빈틈없이 덮으면 더 적은 개수로 덮을 방법이 없습니다.

### ⏱️ 시간 복잡도

기존 기지국 수를 S라 하면 기지국마다 계산을 한 번씩 해 O(S)입니다. n이 2억까지 커도 칸을 하나씩 보지 않습니다.

### 💾 공간 복잡도

몇 개의 변수만 사용하므로 O(1)입니다.

## ⚠️ 실수하기 쉬운 점

- n 크기의 리스트를 만들면 입력이 클 때 메모리와 시간이 부족합니다.
- 기존 기지국의 범위가 겹칠 수 있습니다. 빈 구간이 있을 때만 개수를 더합니다.
- 마지막 기지국 뒤의 빈 구간을 잊기 쉽습니다.

## ✅ 배운 것

연속된 빈칸을 길이 하나로 보고 올림 나눗셈을 쓰면 큰 범위도 빠르게 계산합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 첫 칸이나 마지막 칸에 기존 기지국이 있는 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884) (`42884`) — 범위를 덮는 그리디를 다른 모양으로 복습합니다.
- [최고의 집합](https://school.programmers.co.kr/learn/courses/30/lessons/12938) (`12938`) — 몫과 나머지로 바로 답을 만드는 계산을 연습합니다.
