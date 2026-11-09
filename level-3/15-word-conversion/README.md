# 🧩 단어 변환

- Programmers ID: 43163
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/43163
- Level: 3
- Stage: Level 3 Core 15
- Prerequisites: Level 2 25 BFS, set(), 문자열 인덱싱
- Core concepts: 그래프로 바꿔 생각하기, BFS 최소 단계

## 🎯 이 문제에서 배우는 것

단어를 칸으로, 한 글자 바꾸기를 길로 보고 BFS로 최소 단계를 찾습니다.

## 🔎 문제 핵심

begin에서 target으로 바꾸려 합니다. 한 번에 한 글자만 바꿀 수 있고 바꾼 결과는 words에 있는 단어여야 합니다. 가장 적은 변환 횟수를 돌려주고 바꿀 수 없으면 0입니다.

## 💭 먼저 생각해 보기

"cat"에서 한 번에 갈 수 있는 단어는 words 가운데 어떤 것들인가요? 지도에서 칸을 옮기던 BFS와 어떤 점이 같나요?

## 🧪 예제 이해하기

begin = "cat", target = "dog", words = ["cot", "cog", "dog", "cut"]입니다. cat에서 cot, cut으로 갈 수 있습니다. cot에서 cog, cog에서 dog으로 갑니다. 세 번 바꿔 결과는 3입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

큐에 (단어, 바꾼 횟수)를 넣습니다. 꺼낸 단어와 한 글자만 다른 단어를 아직 방문하지 않았으면 횟수에 1을 더해 넣습니다. target을 꺼내면 그 횟수가 답입니다.

### 🐍 Python 코드

```python
from collections import deque


def solution(begin, target, words):
    def one_letter_apart(first, second):
        differences = 0
        for index in range(len(first)):
            if first[index] != second[index]:
                differences += 1
        return differences == 1

    if target not in words:
        return 0
    visited = set()
    queue = deque([(begin, 0)])
    while queue:
        word, steps = queue.popleft()
        if word == target:
            return steps
        for next_word in words:
            if next_word in visited:
                continue
            if one_letter_apart(word, next_word):
                visited.add(next_word)
                queue.append((next_word, steps + 1))
    return 0
```

### 📖 코드 해설

one_letter_apart는 같은 위치의 글자를 비교해 다른 글자가 정확히 하나인지 확인합니다. 문제의 단어 길이는 모두 같습니다. target이 words에 없으면 도착할 수 없어 바로 0을 돌려줍니다. visited는 이미 큐에 넣은 단어를 기억합니다. 모든 변환의 비용이 1이므로 BFS에서 먼저 꺼낸 target의 횟수가 최솟값입니다.

```text
단계 0  cat
단계 1  cot  cut
단계 2  cog
단계 3  dog
```

### ⏱️ 시간 복잡도

단어 수를 W, 단어 길이를 L이라 합니다. 각 단어를 한 번 꺼내 W개의 단어와 L글자씩 비교해 O(W²L)입니다.

### 💾 공간 복잡도

visited와 큐에 O(W)개의 단어 참조를 저장합니다. 단어 문자열을 새로 복사하지는 않습니다.

## ⚠️ 실수하기 쉬운 점

- begin은 words에 없을 수도 있습니다. 시작 단어는 처음부터 큐에 넣습니다.
- DFS로 처음 찾은 경로는 가장 짧다는 보장이 없습니다.

## ✅ 배운 것

칸이 없는 문제도 상태와 이동 규칙을 정하면 그래프로 보고 BFS를 쓸 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] target에 도달할 수 없는 예와 begin이 words에 있는 예 확인하기

## 🚀 이어 풀어 볼 문제

- [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) (`1844`) — 칸에서 쓰던 BFS를 복습합니다.
- [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189) (`49189`) — 한 지점에서 모든 지점까지의 BFS 거리를 기록합니다.
