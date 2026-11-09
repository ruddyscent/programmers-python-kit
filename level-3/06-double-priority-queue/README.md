# 🧩 이중우선순위큐

- Programmers ID: 42628
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42628
- Level: 3
- Stage: Level 3 Core 06
- Prerequisites: 05 최대 힙, 딕셔너리로 개수 세기, split()
- Core concepts: 두 힙, 늦은 삭제

## 🎯 이 문제에서 배우는 것

두 개의 힙을 함께 쓰고 한쪽에서 지운 값을 다른 쪽에서는 나중에 치우는 방법을 배웁니다.

## 🔎 문제 핵심

operations의 명령을 차례로 처리합니다. "I 숫자"는 숫자를 넣고 "D 1"은 최댓값, "D -1"은 최솟값을 하나 지웁니다. 비어 있을 때의 삭제는 무시합니다. 끝난 뒤 [최댓값, 최솟값]을 돌려주고 비어 있으면 [0, 0]입니다.

## 💭 먼저 생각해 보기

최소 힙 하나만 있으면 최솟값은 쉽게 지웁니다. 최댓값은 어떻게 찾을까요? 최대 힙을 하나 더 두면 한쪽에서 지운 값이 다른 쪽에 남는 문제가 생깁니다.

## 🧪 예제 이해하기

["I 3", "I 8", "I 1", "D 1", "D -1"]이면 3, 8, 1을 넣고 최댓값 8과 최솟값 1을 지웁니다. 3만 남아 결과는 [3, 3]입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

최소 힙과 최대 힙에 같은 값을 넣습니다. counts에는 값마다 실제로 남은 개수를 기록합니다. 힙 맨 앞의 값이 이미 지워졌다면(남은 개수가 0이면) 꺼내 버린 다음 진짜 값을 지웁니다.

### 🐍 Python 코드

```python
from heapq import heappop, heappush


def solution(operations):
    min_heap = []
    max_heap = []
    counts = {}
    size = 0

    def clean(heap, sign):
        while heap and counts.get(sign * heap[0], 0) == 0:
            heappop(heap)

    for operation in operations:
        command, value_text = operation.split()
        value = int(value_text)
        if command == "I":
            heappush(min_heap, value)
            heappush(max_heap, -value)
            counts[value] = counts.get(value, 0) + 1
            size += 1
        elif size > 0:
            if value == 1:
                clean(max_heap, -1)
                removed = -heappop(max_heap)
            else:
                clean(min_heap, 1)
                removed = heappop(min_heap)
            counts[removed] -= 1
            size -= 1

    if size == 0:
        return [0, 0]
    clean(max_heap, -1)
    clean(min_heap, 1)
    return [-max_heap[0], min_heap[0]]
```

### 📖 코드 해설

clean(heap, sign)은 힙 맨 앞에 지워진 값이 있는 동안 계속 꺼냅니다. 최대 힙에는 -value를 넣었으므로 sign = -1을 곱해 원래 값으로 바꾼 뒤 counts를 확인합니다. 한쪽 힙에서 값을 꺼낼 때 다른 쪽 힙은 그대로 둡니다. 그 값이 다른 힙의 맨 앞에 올 때 clean이 치웁니다. 이렇게 필요할 때까지 미뤄 지우는 방법을 늦은 삭제라고 합니다. size는 실제로 남은 값의 수입니다.

```text
넣기 3, 8, 1   min_heap 맨 앞 1   max_heap 맨 앞 -8
D 1  -> max_heap에서 8 제거, counts[8] = 0, min_heap에는 8이 남음
D -1 -> min_heap에서 1 제거, counts[1] = 0
마지막 clean으로 남은 값만 확인 -> [3, 3]
```

같은 값이 여러 번 들어와도 개수로 기록하므로 몇 개가 남았는지 정확히 셀 수 있습니다.

### ⏱️ 시간 복잡도

명령 수를 Q라 하면 각 값은 두 힙에 한 번씩 들어가고 한 번씩 나옵니다. 힙 연산이 O(log Q)라 전체 O(Q log Q)입니다.

### 💾 공간 복잡도

두 힙과 counts에 최대 O(Q)를 저장합니다.

## ⚠️ 실수하기 쉬운 점

- 리스트에서 max()와 remove()로 지우면 명령이 많을 때 매번 전체를 훑어 느립니다.
- 빈 큐에서 삭제 명령이 와도 오류 없이 넘어가야 합니다.
- 마지막 결과를 읽기 전에도 지워진 값을 치워야 합니다.

## ✅ 배운 것

두 힙의 상태가 달라도 실제 개수를 따로 기록하면 지워진 값을 나중에 안전하게 버릴 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 같은 값을 여러 번 넣고 지우는 예를 손으로 따라가기

## 🚀 이어 풀어 볼 문제

- [야근 지수](https://school.programmers.co.kr/learn/courses/30/lessons/12927) (`12927`) — 부호를 바꾼 최대 힙을 복습합니다.
- [디스크 컨트롤러](https://school.programmers.co.kr/learn/courses/30/lessons/42627) (`42627`) — 힙에 여러 기준을 담은 튜플을 넣습니다.
