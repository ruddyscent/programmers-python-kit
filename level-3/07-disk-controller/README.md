# 🧩 디스크 컨트롤러

- Programmers ID: 42627
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42627
- Level: 3
- Stage: Level 3 Core 07
- Prerequisites: 05 힙, 01 튜플 비교, while
- Core concepts: 시간 흐름 모의실행, 우선순위 힙

## 🎯 이 문제에서 배우는 것

시간을 앞으로 옮기며 지금 시작할 수 있는 작업 가운데 가장 우선인 것을 고릅니다.

## 🔎 문제 핵심

jobs[i]는 [요청 시각, 소요 시간]이고 i가 작업 번호입니다. 디스크는 한 번에 하나만 처리하며 시작한 작업은 끝까지 합니다. 쉬고 있을 때 기다리는 작업이 있으면 소요 시간이 짧은 것, 요청이 빠른 것, 번호가 작은 것 순서로 고릅니다. 각 작업의 (끝난 시각 - 요청 시각)의 평균에서 소수점 아래를 버려 돌려줍니다.

## 💭 먼저 생각해 보기

시각 0에 길이 10인 작업만 요청되었고 시각 1에 길이 1인 작업이 들어오면 어떻게 될까요? 디스크가 쉬는 동안 아무 요청도 없다면 시간은 어디로 옮겨야 할까요?

## 🧪 예제 이해하기

jobs = [[0, 4], [1, 2], [2, 1]]입니다. 시각 0에는 0번만 있어 0~4를 처리합니다. 시각 4에 1번(길이 2)과 2번(길이 1)이 기다려 2번을 먼저 4~5, 1번을 5~7에 처리합니다. 걸린 시간은 4, 6, 3이고 평균 13 / 3의 정수 부분 4가 결과입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

작업을 요청 시각 순서로 정렬합니다. 현재 시각까지 요청된 작업을 모두 힙에 넣고 힙이 비어 있지 않으면 하나를 꺼내 처리합니다. 힙이 비어 있으면 다음 요청 시각으로 시간을 건너뜁니다.

### 🐍 Python 코드

```python
from heapq import heappop, heappush


def solution(jobs):
    tasks = []
    for number in range(len(jobs)):
        request, duration = jobs[number]
        tasks.append((request, duration, number))
    tasks.sort()

    waiting = []
    time = 0
    next_task = 0
    finished = 0
    total_turnaround = 0
    while finished < len(tasks):
        while next_task < len(tasks) and tasks[next_task][0] <= time:
            request, duration, number = tasks[next_task]
            heappush(waiting, (duration, request, number))
            next_task += 1
        if waiting:
            duration, request, number = heappop(waiting)
            time += duration
            total_turnaround += time - request
            finished += 1
        else:
            time = tasks[next_task][0]
    return total_turnaround // len(jobs)
```

### 📖 코드 해설

힙에는 (소요 시간, 요청 시각, 번호) 튜플을 넣습니다. 튜플은 앞에서부터 비교하므로 문제의 세 우선순위가 그대로 지켜집니다. next_task는 아직 힙에 넣지 않은 작업 가운데 요청이 가장 빠른 작업의 위치입니다. 작업을 처리하면 time에 소요 시간을 더하고 time - request를 합계에 더합니다. 기다리는 작업이 없으면 다음 요청 시각으로 time을 옮깁니다. 끝으로 //로 평균의 정수 부분을 구합니다.

```text
시각 0    4    5    7
     [0번 ][2][ 1번 ]
```

### ⏱️ 시간 복잡도

작업 수를 N이라 하면 정렬이 O(N log N)입니다. 각 작업은 힙에 한 번 들어가고 한 번 나오며 힙 연산은 O(log N)입니다. 전체 O(N log N)입니다.

### 💾 공간 복잡도

정렬한 작업 리스트와 힙에 O(N)을 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 쉬는 동안 시간을 1씩 늘리면 요청 시각이 멀리 떨어진 경우 반복이 많아집니다. 다음 요청 시각으로 바로 옮깁니다.
- 아직 요청되지 않은 작업을 힙에 미리 넣으면 미래의 작업을 먼저 처리하게 됩니다.
- 작업이 끝나는 시각에 들어온 요청도 고를 수 있도록 <=로 비교합니다.

## ✅ 배운 것

시간 순서로 사건을 처리하면서 지금 고를 수 있는 후보만 힙에 모아 우선순위대로 꺼냅니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 요청 사이에 디스크가 쉬는 예와 우선순위가 같은 작업 예 확인하기

## 🚀 이어 풀어 볼 문제

- [프로세스](https://school.programmers.co.kr/learn/courses/30/lessons/42587) (`42587`) — 우선순위에 따라 처리 순서를 정하는 모의실행을 복습합니다.
- [선입 선출 스케줄링](https://school.programmers.co.kr/learn/courses/30/lessons/12920) (`12920`) — 시간에 따라 작업을 나누는 다른 규칙을 살펴봅니다.
