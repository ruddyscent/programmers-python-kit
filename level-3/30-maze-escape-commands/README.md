# 🧩 미로 탈출 명령어

- Programmers ID: 150365
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/150365
- Level: 3
- Stage: Level 3 Core 30
- Prerequisites: abs(), 홀짝, 튜플 리스트, break
- Core concepts: 사전순 그리디, 남은 거리 확인

## 🎯 이 문제에서 배우는 것

한 글자씩 사전순으로 가장 앞선 선택을 하되, 남은 이동으로 목적지에 갈 수 있는지 확인합니다.

## 🔎 문제 핵심

n × m 격자에서 (x, y)에서 출발해 (r, c)로 가려 합니다. 위치는 (행, 열)이고 1부터 셉니다. 정확히 k번 움직이며 격자 밖으로 나갈 수 없고 같은 칸을 여러 번 지나도 됩니다. 이동은 d(아래), l(왼쪽), r(오른쪽), u(위)로 적습니다. 가능한 경로 문자열 중 사전순으로 가장 앞선 것을 돌려주고 불가능하면 "impossible"입니다.

## 💭 먼저 생각해 보기

목적지까지의 최소 이동 수가 5인데 k가 6이면 갈 수 있을까요? 한 칸 갔다 돌아오면 이동 수가 몇씩 늘어나나요? 사전순으로 앞서려면 첫 글자로 무엇을 먼저 시도해야 할까요?

## 🧪 예제 이해하기

n = 3, m = 3, 출발 (1, 1), 도착 (1, 2), k = 3입니다. 최소 거리는 1이고 남는 이동 2는 짝수라 가능합니다. 첫 글자로 d를 시도하면 (2, 1)이고 남은 2번으로 (1, 2)까지 거리 2라 갈 수 있습니다. 다음에 d는 (3, 1)로 거리 3이라 안 되고, l은 격자 밖이라 안 됩니다. r로 (2, 2)에 가고 마지막에 u로 도착합니다. 결과는 "dru"입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

맨해튼 거리(행 차이 + 열 차이)가 k보다 크거나, 남는 이동 수가 홀수면 불가능합니다. 가능하다면 매 걸음 d, l, r, u 순서로 시도해 격자 안이고 남은 이동 수로 목적지까지 갈 수 있는 첫 방향을 고릅니다.

### 🐍 Python 코드

```python
def solution(n, m, x, y, r, c, k):
    distance = abs(x - r) + abs(y - c)
    if distance > k or (k - distance) % 2 == 1:
        return "impossible"

    moves = [("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0)]
    path = []
    row = x
    column = y
    for step in range(k):
        remaining = k - step - 1
        for letter, row_change, column_change in moves:
            next_row = row + row_change
            next_column = column + column_change
            if not (1 <= next_row <= n and 1 <= next_column <= m):
                continue
            if abs(next_row - r) + abs(next_column - c) <= remaining:
                path.append(letter)
                row = next_row
                column = next_column
                break
    return "".join(path)
```

### 📖 코드 해설

한 칸 움직일 때마다 목적지까지의 거리는 1 늘거나 1 줄어듭니다. 그래서 (k - 거리)가 홀수면 정확히 k번 만에 도착할 수 없습니다. 짝수면 남는 이동을 두 번씩 갔다 돌아오는 데 쓰면 됩니다. 문제에서 n, m이 2 이상이라 왕복할 이웃 칸이 항상 있습니다.

moves는 사전순 d < l < r < u 순서로 적었습니다. 앞 글자가 작을수록 문자열 전체가 앞서므로, 지금 가능한 가장 작은 글자를 고르는 것이 답을 잃지 않습니다. 이동 후 목적지까지의 거리가 remaining 이하인지 확인합니다. 홀짝은 처음 확인으로 이미 맞춰져 있고 걸음마다 거리와 남은 수가 함께 바뀌어 계속 유지됩니다.

```text
출발 (1,1)  d -> (2,1)  남은 2, 거리 2  가능
            r -> (2,2)  남은 1, 거리 1  가능
            u -> (1,2)  남은 0, 도착
```

### ⏱️ 시간 복잡도

걸음마다 네 방향만 확인하므로 O(k)입니다.

### 💾 공간 복잡도

경로 글자 k개를 저장해 반환값을 포함한 추가 공간은 O(k)입니다.

## ⚠️ 실수하기 쉬운 점

- 모든 경로를 DFS로 만들면 4^k개라 끝나지 않습니다.
- x와 r은 행, y와 c는 열입니다. 아래(d)는 행이 1 커집니다.
- 홀짝 확인을 빼먹으면 거리 조건만 맞고 도착할 수 없는 경우가 생깁니다.

## ✅ 배운 것

사전순으로 가장 앞선 답은 앞 글자부터 가장 작은 선택을 고르고 그 선택 뒤에도 답이 남는지 확인해 만듭니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 홀짝이 맞지 않는 예와 격자 가장자리에서 출발하는 예 확인하기

## 🚀 이어 풀어 볼 문제

- [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) (`1844`) — 격자에서 방향과 범위를 확인하는 코드를 복습합니다.
- [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164) (`43164`) — 사전순으로 앞선 답을 찾는 다른 방법과 비교합니다.
