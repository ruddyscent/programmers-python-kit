# 🧩 보석 쇼핑

- Programmers ID: 67258
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/67258
- Level: 3
- Stage: Level 3 Core 13
- Prerequisites: set(), 딕셔너리로 개수 세기, del, Level 2 04 두 포인터
- Core concepts: 슬라이딩 윈도우, 두 포인터

## 🎯 이 문제에서 배우는 것

구간의 양 끝을 앞으로만 움직이며 조건을 만족하는 가장 짧은 구간을 찾습니다.

## 🔎 문제 핵심

진열대 gems에 보석 이름이 차례로 있습니다. 모든 종류를 하나 이상 포함하는 연속 구간 가운데 가장 짧은 것을 찾아 [시작 번호, 끝 번호]로 돌려줍니다. 번호는 1부터 셉니다. 가장 짧은 구간이 여러 개면 시작 번호가 가장 작은 것을 돌려줍니다.

## 💭 먼저 생각해 보기

끝을 한 칸씩 늘리다가 모든 종류가 들어온 순간을 떠올려 보세요. 이때 시작 쪽에서 빼도 괜찮은 보석은 무엇인가요?

## 🧪 예제 이해하기

gems = ["A", "B", "A", "C", "B"]이면 종류는 3개입니다. 1~4번 구간에 A, B, C가 모두 있고 시작 A를 빼도 2~4번에 B, A, C가 남습니다. 길이 3인 2~4번이 가장 짧은 구간이라 결과는 [2, 4]입니다. 3~5번도 길이 3이지만 시작 번호가 더 큽니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

end를 한 칸씩 늘려 보석을 구간에 넣습니다. 구간에 모든 종류가 있는 동안 답을 갱신하고 start의 보석을 빼며 구간을 줄입니다.

### 🐍 Python 코드

```python
def solution(gems):
    kinds = len(set(gems))
    counts = {}
    best_start = 0
    best_end = len(gems) - 1
    start = 0
    for end in range(len(gems)):
        gem = gems[end]
        counts[gem] = counts.get(gem, 0) + 1
        while len(counts) == kinds:
            if end - start < best_end - best_start:
                best_start = start
                best_end = end
            start_gem = gems[start]
            counts[start_gem] -= 1
            if counts[start_gem] == 0:
                del counts[start_gem]
            start += 1
    return [best_start + 1, best_end + 1]
```

### 📖 코드 해설

counts는 현재 구간 안의 보석 종류별 개수입니다. 개수가 0이 되면 del로 키를 지웁니다. 그래서 len(counts)가 곧 구간 안의 종류 수입니다. 모든 종류가 들어 있는 동안 현재 구간을 답과 비교하고 start를 한 칸 옮깁니다. 같은 길이의 구간은 시작이 작은 것을 먼저 만나므로 더 짧을 때만 답을 바꿉니다.

창문을 밀듯이 구간이 오른쪽으로 움직여 이 방법을 슬라이딩 윈도우라고도 합니다.

```text
A B A C B
[-----]      start=0, end=3  모든 종류, 길이 4
  [---]      start=1, end=3  모든 종류, 길이 3  답 갱신
    [-]      start=2, end=3  B가 빠져 멈춤
    [---]    start=2, end=4  모든 종류, 길이 3  같은 길이라 유지
```

### ⏱️ 시간 복잡도

보석 수를 N이라 합니다. start와 end는 각각 최대 N번 앞으로만 움직여 전체 O(N)입니다. 보석 이름은 짧아 해시 계산을 한 번으로 셉니다.

### 💾 공간 복잡도

종류 수를 K라 하면 set과 counts에 O(K)를 사용합니다. set을 만들 때 잠깐 쓰는 공간도 O(K)입니다.

## ⚠️ 실수하기 쉬운 점

- 모든 시작과 끝을 둘 다 반복하면 O(N²)이라 10만 개에서 느립니다.
- 개수가 0인 키를 지우지 않으면 len(counts)가 실제 종류 수보다 커집니다.
- 반환할 때 0부터 센 위치에 1을 더합니다.

## ✅ 배운 것

두 위치가 모두 앞으로만 움직이게 만들면 연속 구간 문제를 한 번의 훑기로 풀 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 종류가 하나뿐인 경우와 같은 길이 구간이 여러 개인 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [숫자의 표현](https://school.programmers.co.kr/learn/courses/30/lessons/12924) (`12924`) — 두 포인터로 연속 구간의 합을 다룬 방법을 복습합니다.
- [연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701) (`131701`) — 연속 구간을 모두 볼 때와 줄여서 볼 때를 비교합니다.
