# 🧩 징검다리 건너기

- Programmers ID: 64062
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/64062
- Level: 3
- Stage: Level 3 Core 12
- Prerequisites: 11 이분 탐색, 연속 개수 세기
- Core concepts: 가장 큰 답 찾기, 조건 확인 함수

## 🎯 이 문제에서 배우는 것

"이만큼은 가능한가?"를 확인하는 함수를 만들고 가능한 가장 큰 값을 이분 탐색으로 찾습니다.

## 🔎 문제 핵심

stones에는 디딤돌마다 밟을 수 있는 횟수가 적혀 있습니다. 한 사람이 건널 때 밟은 돌의 숫자가 1씩 줄고 0이 된 돌은 밟을 수 없습니다. 사람은 다음 돌로 건너뛸 수 있는데 한 번에 최대 k칸까지만 이동합니다. 최대 몇 명이 건널 수 있는지 돌려줍니다.

## 💭 먼저 생각해 보기

친구 m명이 건너려면 m번째 사람이 건널 때 어떤 돌이 이미 0이 되어 있을까요? 숫자가 m보다 작은 돌이 몇 개 연속되면 건널 수 없나요?

## 🧪 예제 이해하기

stones = [3, 1, 2, 4, 5], k = 2입니다. 첫 사람이 지나면 [2, 0, 1, 3, 4]가 되고 두 번째 사람은 0이 된 돌 하나를 건너뛰어 지나갑니다. 그러면 [1, 0, 0, 2, 3]이 되어 세 번째 사람은 3칸을 뛰어야 하므로 건널 수 없습니다. 결과는 2입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

m명이 건널 수 있으려면 숫자가 m보다 작은 돌이 k개 연속되면 안 됩니다. m이 커질수록 조건은 어려워지므로, 가능한 가장 큰 m을 이분 탐색으로 찾습니다.

### 🐍 Python 코드

```python
def solution(stones, k):
    def can_cross(friends):
        sunken_in_row = 0
        for stone in stones:
            if stone < friends:
                sunken_in_row += 1
                if sunken_in_row == k:
                    return False
            else:
                sunken_in_row = 0
        return True

    low = 1
    high = max(stones)
    while low < high:
        middle = (low + high + 1) // 2
        if can_cross(middle):
            low = middle
        else:
            high = middle - 1
    return low
```

### 📖 코드 해설

can_cross(friends)는 숫자가 friends보다 작은 돌의 연속 개수를 셉니다. 사람마다 밟는 돌의 숫자가 1씩 줄기 때문에, friends번째 사람 앞에서 숫자가 friends - 1 이하였던 돌은 이미 0입니다. 그런 돌이 k개 연속이면 k + 1칸을 뛰어야 해서 실패입니다.

11번과 달리 이번에는 가능한 가장 큰 값을 찾습니다. 가능하면 low = middle, 불가능하면 high = middle - 1입니다. middle을 (low + high + 1) // 2로 올려 계산해야 low와 high가 하나 차이일 때 범위가 줄어듭니다. 한 명은 늘 건널 수 있고 max(stones)명보다 많이 건널 수는 없어서 범위를 1부터 max(stones)까지로 정했습니다.

```text
돌         3 1 2 4 5
2명 기준   o x o o o   숫자 < 2인 연속 돌 1개 -> 가능
3명 기준   o x x o o   숫자 < 3인 연속 돌 2개 -> 불가능
```

### ⏱️ 시간 복잡도

돌 수를 N, 가장 큰 돌의 숫자를 V라 합니다. 확인 함수가 O(N)이고 O(log V)번 호출해 전체 O(N log V)입니다.

### 💾 공간 복잡도

변수 몇 개만 사용하므로 O(1)입니다.

## ⚠️ 실수하기 쉬운 점

- 사람을 한 명씩 실제로 건너게 하면 돌 숫자가 2억까지 커서 시간이 부족합니다.
- 가장 큰 답을 찾을 때 middle을 내림으로 계산하면 반복이 끝나지 않을 수 있습니다.

## ✅ 배운 것

가장 큰 답을 찾을 때는 조건을 만족하면 low를 middle로 옮기고 middle은 올림으로 계산합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] k가 1인 경우와 k가 돌 수와 같은 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) (`43238`) — 가장 작은 답을 찾는 이분 탐색과 비교합니다.
- [보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258) (`67258`) — 연속 구간을 다루는 다른 방법을 배웁니다.
