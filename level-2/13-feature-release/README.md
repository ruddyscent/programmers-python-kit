# 🧩 기능개발

- Programmers ID: 42586
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42586
- Level: 2
- Stage: Level 2 Core 13
- Prerequisites: 같은 위치의 두 리스트, //, 순회
- Core concepts: 큐의 순서, 완료 일수와 배포 일수

## 🎯 이 문제에서 배우는 것

먼저 끝나는 시점과 실제로 함께 나가는 시점을 구별합니다.

## 🔎 문제 핵심

progresses의 기능들은 speeds만큼 하루에 진도가 늘어납니다. 앞 기능이 먼저 배포되어야 하므로 뒤 기능이 먼저 끝나면 기다립니다. 각 배포의 기능 개수를 순서대로 돌려줍니다.

## 💭 먼저 생각해 보기

완료에 걸리는 날이 5일, 2일, 6일인 세 기능은 몇 묶음으로 나갈까요?

## 🧪 예제 이해하기

progresses = [80, 90, 70], speeds = [4, 5, 5]이면 완료 일수는 [5, 2, 6]입니다. 앞 두 기능은 5일째 함께, 마지막은 6일째 나가 결과는 [2, 1]입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

각 기능의 완료 일수를 구합니다. 현재 묶음의 배포일보다 늦게 끝나는 기능을 만나면 새 묶음을 시작합니다.

### 🐍 Python 코드

```python
def solution(progresses, speeds):
    batches = []
    release_day = 0
    for index in range(len(progresses)):
        remaining = 100 - progresses[index]
        speed = speeds[index]
        days = (remaining + speed - 1) // speed
        if days > release_day:
            release_day = days
            batches.append(1)
        else:
            batches[-1] += 1
    return batches
```

### 📖 코드 해설

(remaining + speed - 1) // speed는 나눗셈의 올림을 정수로 구합니다. 7만큼 남고 속도가 3이면 3일이 필요합니다. 처음 기능은 완료에 하루 이상 걸려 새 묶음을 만듭니다. 먼저 들어온 항목을 먼저 처리하는 순서를 큐라고 부릅니다. 여기서는 앞에서부터 한 번 읽기만 해도 순서를 지킬 수 있어 별도 큐가 필요 없습니다.

### ⏱️ 시간 복잡도

기능 수 N에 대해 일수 계산과 묶음 처리를 한 번씩 하므로 O(N)입니다.

### 💾 공간 복잡도

반환 리스트에 최대 N개 묶음을 저장합니다. 반환값 포함 O(N), 반환값 제외 O(1)입니다.

## ⚠️ 실수하기 쉬운 점

- 완료 일수를 정렬하면 앞 기능을 기다려야 하는 규칙을 잃습니다.
- 나누어 떨어지지 않을 때 하루를 더 기다려야 합니다.

## ✅ 배운 것

완료 일수와 배포 일수를 구별하면 날마다 진도를 갱신하지 않고 묶음을 구할 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 완료 일수가 같거나 뒤 기능이 훨씬 먼저 끝나는 경우 설명하기

## 🚀 이어 풀어 볼 문제

- [프로세스](https://school.programmers.co.kr/learn/courses/30/lessons/42587) (`42587`) — 대기 항목을 앞에서 꺼내고 뒤에 다시 넣습니다.
- [주식가격](https://school.programmers.co.kr/learn/courses/30/lessons/42584) (`42584`) — 시간이 지난 뒤 각 항목의 결과를 정합니다.
