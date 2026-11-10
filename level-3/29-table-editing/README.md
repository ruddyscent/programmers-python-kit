# 🧩 표 편집

- Programmers ID: 81303
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/81303
- Level: 3
- Stage: Level 3 Core 29
- Prerequisites: Level 2 12 스택, split(), join()
- Core concepts: 연결 리스트, 위아래 이웃 기록, 되돌리기 스택

## 🎯 이 문제에서 배우는 것

리스트에서 실제로 지우지 않고 위아래 이웃만 바꿔 삭제와 복구를 빠르게 처리합니다.

## 🔎 문제 핵심

n개의 행이 있는 표에서 처음 선택된 행은 k번입니다. cmd의 명령은 "U X"(X칸 위로), "D X"(X칸 아래로), "C"(선택 행 삭제 후 바로 아래 행 선택, 마지막 행이었다면 바로 위 행 선택), "Z"(가장 최근 삭제 행을 원래 자리에 복구)입니다. 모든 명령 후 처음 행 번호 순서대로 남아 있으면 "O", 삭제되었으면 "X"인 문자열을 돌려줍니다.

## 💭 먼저 생각해 보기

행이 100만 개인 리스트에서 가운데 행을 pop()하면 뒤의 행들이 모두 한 칸씩 당겨집니다. 각 행이 자기 바로 위와 아래 행만 알고 있다면, 삭제할 때 몇 개의 값만 바꾸면 될까요?

## 🧪 예제 이해하기

n = 4, k = 1, cmd = ["C", "C", "Z"]입니다. 1번을 지우면 2번이 선택되고, 2번을 지우면 3번이 선택됩니다. Z로 2번을 복구해도 선택은 3번입니다. 1번만 삭제 상태라 결과는 "OXOO"입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

above[row]와 below[row]에 바로 위와 아래에 남아 있는 행 번호를 저장합니다. 삭제는 위아래 행이 서로를 가리키게 하고 삭제한 행은 스택에 넣습니다. 복구는 스택에서 꺼낸 행의 위아래 행이 다시 이 행을 가리키게 합니다.

### 🐍 Python 코드

```python
def solution(n, k, cmd):
    above = []
    below = []
    for row in range(n):
        above.append(row - 1)
        below.append(row + 1)
    below[n - 1] = -1

    deleted = [False] * n
    removed = []
    current = k
    for command in cmd:
        parts = command.split()
        if parts[0] == "U":
            for step in range(int(parts[1])):
                current = above[current]
        elif parts[0] == "D":
            for step in range(int(parts[1])):
                current = below[current]
        elif parts[0] == "C":
            deleted[current] = True
            removed.append(current)
            up = above[current]
            down = below[current]
            if up != -1:
                below[up] = down
            if down != -1:
                above[down] = up
            if down != -1:
                current = down
            else:
                current = up
        else:
            row = removed.pop()
            deleted[row] = False
            up = above[row]
            down = below[row]
            if up != -1:
                below[up] = row
            if down != -1:
                above[down] = row

    marks = []
    for row in range(n):
        if deleted[row]:
            marks.append("X")
        else:
            marks.append("O")
    return "".join(marks)
```

### 📖 코드 해설

-1은 위나 아래에 행이 없다는 뜻입니다. 이처럼 각 칸이 이웃을 가리키며 이어지는 구조를 연결 리스트라고 합니다.

삭제된 행의 above와 below 값은 그대로 둡니다. 복구는 가장 최근 삭제부터 거꾸로 하므로, 복구하는 순간 그 행이 기억한 위아래 행은 삭제 당시처럼 표에 남아 있습니다. 그래서 그 두 행이 다시 이 행을 가리키게만 하면 원래 자리로 돌아옵니다.

```text
처음      0 <-> 1 <-> 2 <-> 3
1 삭제    0 <-------> 2 <-> 3     1은 여전히 위=0, 아래=2를 기억
1 복구    0 <-> 1 <-> 2 <-> 3     0과 2가 다시 1을 가리킴
```

U와 D는 이웃을 X번 따라갑니다. 문제에서 모든 X의 합이 100만 이하로 제한되어 이동 횟수가 많지 않습니다.

### ⏱️ 시간 복잡도

행 수를 n, 명령 수를 Q, 이동 칸 수의 합을 M이라 합니다. 준비와 답 만들기에 O(n), 삭제와 복구는 명령마다 O(1), 이동은 전체 O(M)이라 전체 O(n + Q + M)입니다.

### 💾 공간 복잡도

above, below, deleted, marks에 O(n), 삭제 스택에 최대 O(Q)를 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 실제 리스트에서 행을 지우고 끼우면 한 번에 O(n)이 걸려 느립니다.
- 마지막 행을 지우면 위 행을 선택해야 합니다.
- 복구는 선택 행을 바꾸지 않습니다.

## ✅ 배운 것

위아래 이웃만 바꾸는 연결 리스트와 되돌리기 스택을 함께 쓰면 삭제와 복구를 바로 처리할 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 첫 행과 마지막 행을 지우고 복구하는 예를 손으로 따라가기

## 🚀 이어 풀어 볼 문제

- [짝지어 제거하기](https://school.programmers.co.kr/learn/courses/30/lessons/12973) (`12973`) — 마지막에 넣은 것을 먼저 꺼내는 스택을 복습합니다.
- [이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628) (`42628`) — 실제로 지우는 대신 상태를 기록하는 방법을 비교합니다.
