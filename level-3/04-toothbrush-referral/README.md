# 🧩 다단계 칫솔 판매

- Programmers ID: 77486
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/77486
- Level: 3
- Stage: Level 3 Core 04
- Prerequisites: 딕셔너리, while, 몫 //
- Core concepts: 부모를 따라 올라가기, 트리

## 🎯 이 문제에서 배우는 것

각 사람이 자기 추천인만 기억하는 구조에서 위쪽으로 돈을 나눠 보냅니다.

## 🔎 문제 핵심

enroll[i]의 추천인은 referral[i]이고 "-"는 맨 위 센터입니다. seller[i]가 칫솔 amount[i]개를 팔면 개당 100원의 이익이 생깁니다. 이익의 10%를 원 단위 아래는 버리고 추천인에게 넘기고 나머지를 갖습니다. 넘겨받은 사람도 같은 규칙으로 위에 넘깁니다. 10%가 1원보다 작으면 넘기지 않습니다. enroll 순서대로 각자의 총이익을 돌려줍니다.

## 💭 먼저 생각해 보기

판매 이익이 1,000원이면 판매자, 추천인, 그 위 추천인은 각각 얼마를 갖게 될까요? 금액이 0이 되면 더 올라갈 필요가 있나요?

## 🧪 예제 이해하기

센터 아래 "kim", kim 아래 "lee"가 있고 lee가 칫솔 2개를 팔았습니다. 이익 200원 중 lee가 180원, kim에게 20원이 갑니다. kim은 18원을 갖고 센터에 2원을 넘깁니다. 결과는 enroll 순서에 따라 kim 18, lee 180입니다.

```text
center <- 2원
  kim  : 20원 받아 18원 보관
   lee : 200원 벌어 180원 보관
```

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

이름을 키로 추천인과 이익을 저장합니다. 판매마다 판매자에서 출발해 넘길 금액이 없거나 센터에 닿을 때까지 위로 올라갑니다.

### 🐍 Python 코드

```python
def solution(enroll, referral, seller, amount):
    parent = {}
    profit = {}
    for index in range(len(enroll)):
        parent[enroll[index]] = referral[index]
        profit[enroll[index]] = 0

    for index in range(len(seller)):
        person = seller[index]
        money = amount[index] * 100
        while person != "-" and money > 0:
            share = money // 10
            profit[person] += money - share
            person = parent[person]
            money = share

    answer = []
    for name in enroll:
        answer.append(profit[name])
    return answer
```

### 📖 코드 해설

parent는 사람마다 바로 위 추천인을 기억합니다. 한 사람이 부모를 하나씩 가리키는 이 모양을 트리라고 합니다. share = money // 10이 위로 넘길 몫이고 money - share를 자기 이익에 더합니다. 그다음 person과 money를 위 사람과 넘긴 금액으로 바꿉니다. money가 10원보다 작으면 share가 0이 되고 그 사람이 전부 가집니다. 다음 반복에서 money가 0이라 멈춥니다.

### ⏱️ 시간 복잡도

판매 기록 수를 S, 사람 수를 P라 합니다. 한 판매의 이익은 최대 10,000원이고 한 단계 올라갈 때마다 10분의 1이 되어 다섯 단계 안에 0이 됩니다. 그래서 판매 처리는 O(S)이고 딕셔너리 준비와 답 만들기에 O(P)가 듭니다. 이름은 짧아 해시 계산을 한 번으로 셉니다.

### 💾 공간 복잡도

두 딕셔너리와 반환 리스트에 O(P)를 사용합니다.

## ⚠️ 실수하기 쉬운 점

- 10%를 판매 금액 전체가 아니라 각자 받은 금액에서 계산합니다.
- 같은 사람이 여러 번 판매할 수 있으므로 판매마다 따로 나눕니다. 판매량을 먼저 합치면 버림 결과가 달라질 수 있습니다.
- 금액이 0이 된 뒤에도 끝까지 올라가면 사람 수가 많을 때 느려집니다.

## ✅ 배운 것

부모만 기억해도 위로 올라가는 계산을 할 수 있고 줄어드는 금액이 반복 횟수를 제한합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 1원짜리 몫이 생기는 경우와 같은 사람이 두 번 판매하는 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [베스트앨범](https://school.programmers.co.kr/learn/courses/30/lessons/42579) (`42579`) — 이름을 키로 값을 모으는 딕셔너리 활용을 복습합니다.
- [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971) (`86971`) — 트리의 연결을 다른 방향에서 살펴봅니다.
