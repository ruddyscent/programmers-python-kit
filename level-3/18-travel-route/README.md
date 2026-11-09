# 🧩 여행경로

- Programmers ID: 43164
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/43164
- Level: 3
- Stage: Level 3 Core 18
- Prerequisites: Level 2 24 재귀, 딕셔너리, 튜플 정렬
- Core concepts: 백트래킹, 사전순 우선 탐색

## 🎯 이 문제에서 배우는 것

선택했다가 막히면 되돌리는 백트래킹으로 모든 항공권을 쓰는 경로를 찾습니다.

## 🔎 문제 핵심

tickets의 각 항목은 [출발 공항, 도착 공항]입니다. "ICN"에서 출발해 모든 항공권을 한 번씩 사용하는 경로를 공항 이름 리스트로 돌려줍니다. 가능한 경로가 여러 개면 알파벳 순서가 앞서는 경로를 돌려주며 모든 항공권을 쓰는 경로는 항상 있습니다.

## 💭 먼저 생각해 보기

ICN에서 갈 수 있는 곳이 AAA와 BBB라면 알파벳이 앞선 AAA부터 가 보는 게 좋습니다. 그런데 AAA로 가면 남은 항공권을 다 쓸 수 없다면 어떻게 해야 할까요?

## 🧪 예제 이해하기

tickets = [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]입니다. ICN에서 AAA로 먼저 가면 AAA에서 나가는 항공권이 없어 두 장이 남습니다. 되돌아와 BBB로 가고, ICN으로 돌아와 AAA로 갑니다. 결과는 ["ICN", "BBB", "ICN", "AAA"]입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

공항마다 출발 항공권을 도착 공항의 알파벳 순서로 정렬합니다. 현재 공항에서 아직 쓰지 않은 항공권을 하나 써 보고 재귀로 이어 갑니다. 모든 항공권을 쓰면 성공입니다. 막히면 항공권을 되돌려 놓고 다음 항공권을 시도합니다.

### 🐍 Python 코드

```python
import sys


def solution(tickets):
    sys.setrecursionlimit(20000)
    routes = {}
    for index in range(len(tickets)):
        start, end = tickets[index]
        if start not in routes:
            routes[start] = []
        routes[start].append((end, index))
    for start in routes:
        routes[start].sort()

    used = [False] * len(tickets)
    path = ["ICN"]

    def travel(airport):
        if len(path) == len(tickets) + 1:
            return True
        for end, index in routes.get(airport, []):
            if used[index]:
                continue
            used[index] = True
            path.append(end)
            if travel(end):
                return True
            used[index] = False
            path.pop()
        return False

    travel("ICN")
    return path
```

### 📖 코드 해설

routes는 출발 공항마다 (도착 공항, 항공권 번호) 목록을 저장합니다. 같은 구간의 항공권이 여러 장일 수 있어 번호로 각각 구별합니다. used[index]는 그 항공권을 이미 썼는지 표시합니다.

travel은 성공하면 True를 돌려줍니다. 성공하는 순간 바로 True를 위로 전달해 더 찾지 않습니다. 알파벳 순서로 시도하므로 처음 찾은 완성 경로가 사전순으로 가장 앞섭니다. 실패하면 used와 path를 시도 전 상태로 되돌립니다. 이렇게 시도하고 되돌리는 방법을 백트래킹이라고 합니다.

항공권이 최대 10,000장이라 재귀가 10,000번 넘게 겹칠 수 있습니다. Python은 기본으로 약 1,000번까지만 겹친 재귀를 허락합니다. 그래서 sys.setrecursionlimit()로 한도를 늘렸습니다.

```text
ICN -> AAA  (남은 항공권이 있는데 갈 곳 없음, 되돌림)
ICN -> BBB -> ICN -> AAA  (모두 사용, 성공)
```

### ⏱️ 시간 복잡도

항공권 수를 T라 합니다. 막히는 일이 없으면 각 공항의 목록을 훑으며 O(T²) 안에 끝나고 정렬은 O(T log T)입니다. 하지만 백트래킹은 막힌 길을 되돌아가 다시 시도하므로 나쁜 입력에서는 시도 횟수가 지수적으로 늘 수 있습니다. 로컬 검사에서는 항공권 10,000장이 한 줄로 이어진 입력을 확인했지만 모든 입력의 시간을 보장하지는 않습니다.

### 💾 공간 복잡도

routes, used, path에 O(T), 재귀 호출에 최대 O(T)를 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 알파벳 순서로 가장 앞선 곳에 무조건 가면 항공권을 다 쓰지 못할 수 있습니다.
- 같은 출발·도착 항공권이 두 장이면 각각 따로 써야 합니다. 방문 여부를 공항이 아니라 항공권으로 기록합니다.
- 실패한 뒤 used와 path를 되돌리지 않으면 다음 시도가 틀어집니다.

## ✅ 배운 것

순서대로 시도하고 실패하면 상태를 되돌리는 백트래킹은 조건을 모두 만족하는 첫 경로를 찾는 데 쓰입니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 같은 항공권이 두 장인 예와 되돌아가야 하는 예를 손으로 따라가기

## 🚀 이어 풀어 볼 문제

- [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) (`43165`) — 재귀로 선택의 나무를 탐색한 경험을 복습합니다.
- [불량 사용자](https://school.programmers.co.kr/learn/courses/30/lessons/64064) (`64064`) — 선택하고 되돌리는 백트래킹을 다른 조건에 씁니다.
