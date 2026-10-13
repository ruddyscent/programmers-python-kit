# 🧩 프로세스

- Programmers ID: 42587
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42587
- Level: 2
- Stage: Level 2 Core 14
- Prerequisites: 13 기능개발, 리스트와 튜플
- Core concepts: deque, 우선순위에 따른 순서 모의실행

## 🎯 이 문제에서 배우는 것

대기 순서와 중요도를 함께 추적하며 문제의 규칙대로 실행합니다.

## 🔎 문제 핵심

priorities에서 맨 앞 항목을 꺼낸 뒤 더 높은 중요도가 남아 있으면 뒤로 보냅니다. 없으면 실행합니다. 원래 위치 location의 항목이 몇 번째로 실행되는지 돌려줍니다.

## 💭 먼저 생각해 보기

중요도 [1, 3, 2]에 A, B, C 이름을 붙이고 큐 앞에서 꺼내는 과정을 손으로 써 보세요.

## 🧪 예제 이해하기

처음 A를 뒤로 보내 큐는 B, C, A가 됩니다. 이후 B, C, A 순서로 실행됩니다. location = 0이면 결과는 3입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

원래 위치와 중요도를 짝지어 deque에 넣습니다. 앞에서 꺼낸 뒤 더 높은 중요도가 있으면 다시 넣고 없으면 실행 횟수를 늘립니다.

### 🐍 Python 코드

```python
from collections import deque


def solution(priorities, location):
    queue = deque()
    for index in range(len(priorities)):
        queue.append((index, priorities[index]))

    executed = 0
    while queue:
        index, priority = queue.popleft()
        has_higher = False
        for waiting in queue:
            if waiting[1] > priority:
                has_higher = True
                break
        if has_higher:
            queue.append((index, priority))
        else:
            executed += 1
            if index == location:
                return executed
```

### 📖 코드 해설

collections.deque는 양 끝에서 넣고 꺼내기 좋은 표준 라이브러리 자료형입니다. popleft()는 맨 앞 값을 꺼냅니다. 리스트의 pop(0)은 뒤 값들을 당겨야 하지만 deque는 그럴 필요가 없습니다. 위치를 함께 저장해야 중요도가 같은 항목들도 구별할 수 있습니다. 큐가 비지 않은 동안 while queue가 참입니다.

### ⏱️ 시간 복잡도

항목 수를 N이라 하면 한 번의 중요도 검사에 최대 O(N)이 듭니다. 중요도가 1부터 9로 제한되어 각 단계에서 큐를 많아야 한 바퀴씩 확인하므로 꺼내기는 O(9N)번, 전체 최악 O(N²)입니다.

### 💾 공간 복잡도

큐에 최대 N개의 위치·중요도 쌍을 저장합니다. 반환값을 포함한 추가 공간은 O(N)입니다.

## ⚠️ 실수하기 쉬운 점

- 중요도가 같으면 뒤로 보내지 않습니다. 비교는 >입니다.
- location은 이동 중 위치가 아니라 처음 위치입니다.

## ✅ 배운 것

큐는 처리 순서를, 함께 저장한 원래 위치는 항목의 정체를 기억합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 같은 중요도만 있을 때 원래 순서대로 실행되는 이유 설명하기

## 🚀 이어 풀어 볼 문제

- [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) (`42586`) — 먼저 들어온 항목이 기다림에 주는 영향을 비교합니다.
- [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) (`1844`) — 먼저 발견한 칸부터 처리하는 큐를 사용합니다.
