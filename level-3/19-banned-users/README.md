# 🧩 불량 사용자

- Programmers ID: 64064
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/64064
- Level: 3
- Stage: Level 3 Core 19
- Prerequisites: 18 백트래킹, set(), tuple(), sorted()
- Core concepts: 후보 목록, 중복 없는 조합 세기

## 🎯 이 문제에서 배우는 것

선택 순서는 달라도 결과가 같은 경우를 집합으로 한 번만 셉니다.

## 🔎 문제 핵심

user_id는 사용자 아이디, banned_id는 일부 글자를 *로 가린 아이디입니다. *는 아무 글자 하나와 맞고 길이는 같아야 합니다. banned_id의 각 항목에 서로 다른 사용자를 하나씩 대응시킬 때 제재 대상이 될 수 있는 사용자 묶음의 가짓수를 돌려줍니다. 순서가 달라도 사용자가 같으면 같은 묶음입니다.

## 💭 먼저 생각해 보기

"ab*"와 "a*c"가 가린 아이디이고 사용자는 "abc", "abd"입니다. 첫 번째에 abd, 두 번째에 abc를 고르는 경우만 가능할까요? 다른 순서로 같은 두 사람이 나오면 몇 번 세야 할까요?

## 🧪 예제 이해하기

user_id = ["abc", "abd", "acc"], banned_id = ["a*c", "a*c"]입니다. "a*c"에는 abc와 acc가 맞습니다. 두 항목에 서로 다른 사람을 고르면 (abc, acc)와 (acc, abc)인데 같은 묶음입니다. 결과는 1입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

banned_id 항목마다 맞는 사용자 번호 목록을 만듭니다. 항목 순서대로 아직 고르지 않은 사용자를 하나씩 골라 끝까지 가면, 고른 번호를 정렬해 집합에 넣습니다. 집합의 크기가 답입니다.

### 🐍 Python 코드

```python
def solution(user_id, banned_id):
    def matches(user, pattern):
        if len(user) != len(pattern):
            return False
        for index in range(len(user)):
            if pattern[index] != "*" and pattern[index] != user[index]:
                return False
        return True

    candidates = []
    for pattern in banned_id:
        matched = []
        for user_index in range(len(user_id)):
            if matches(user_id[user_index], pattern):
                matched.append(user_index)
        candidates.append(matched)

    found_sets = set()
    chosen = []

    def choose(position):
        if position == len(candidates):
            found_sets.add(tuple(sorted(chosen)))
            return
        for user_index in candidates[position]:
            if user_index in chosen:
                continue
            chosen.append(user_index)
            choose(position + 1)
            chosen.pop()

    choose(0)
    return len(found_sets)
```

### 📖 코드 해설

matches는 길이가 같고, *가 아닌 위치의 글자가 모두 같은지 확인합니다. candidates[position]은 position번째 가린 아이디에 맞는 사용자 번호 목록입니다. choose는 18번처럼 고른 뒤 재귀를 부르고 돌아오면 pop()으로 되돌립니다.

리스트는 집합에 넣을 수 없어 tuple()로 바꿉니다. 정렬해서 넣으므로 고른 순서가 달라도 같은 묶음은 같은 튜플이 됩니다.

```text
a*c -> [abc, acc]
a*c -> [abc, acc]
고른 순서 (abc, acc) -> 정렬 (abc, acc)
고른 순서 (acc, abc) -> 정렬 (abc, acc)  같은 묶음
```

### ⏱️ 시간 복잡도

사용자 수를 U, 가린 아이디 수를 B, 아이디 길이를 L이라 합니다. 후보 목록을 만드는 데 O(UBL)이 걸립니다. 고르는 경우는 최대 U × (U - 1) × … 로 B개를 고르는 수이며, U가 8 이하라 8! = 40,320을 넘지 않습니다. 각 경우에 정렬과 튜플 만들기가 O(B log B)입니다.

### 💾 공간 복잡도

후보 목록에 O(UB), 찾은 묶음 집합에 묶음 수 × B만큼 저장합니다. 묶음 수는 U개 중 B개를 고르는 수를 넘지 않습니다.

## ⚠️ 실수하기 쉬운 점

- 한 사용자를 두 가린 아이디에 동시에 대응시키면 안 됩니다.
- 순서만 다른 경우를 따로 세면 답이 커집니다.
- *의 개수와 상관없이 길이가 다르면 맞지 않습니다.

## ✅ 배운 것

순서가 다른 같은 결과는 정렬해 같은 모양으로 만든 뒤 집합에 넣어 중복을 없앱니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 가린 아이디가 모두 *로만 된 예 확인하기

## 🚀 이어 풀어 볼 문제

- [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) (`87946`) — 모든 순서를 시도하는 완전탐색을 복습합니다.
- [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164) (`43164`) — 선택하고 되돌리는 백트래킹을 다시 써 봅니다.
