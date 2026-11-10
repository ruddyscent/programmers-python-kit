# 🧩 N으로 표현

- Programmers ID: 42895
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42895
- Level: 3
- Stage: Level 3 Core 27
- Prerequisites: set(), 문자열 반복, 중첩 반복
- Core concepts: 사용 횟수별 집합 DP

## 🎯 이 문제에서 배우는 것

N을 k번 써서 만들 수 있는 수를 더 적게 쓴 결과들로 만들어 갑니다.

## 🔎 문제 핵심

숫자 N과 사칙연산만으로 number를 표현할 때 N을 가장 적게 쓰는 횟수를 돌려줍니다. 55처럼 N을 이어 붙인 수도 쓸 수 있고 괄호도 쓸 수 있습니다. 나눗셈의 나머지는 버립니다. 최솟값이 8보다 크면 -1을 돌려줍니다.

## 💭 먼저 생각해 보기

N = 3일 때 3을 한 번 쓰면 3을 만듭니다. 두 번 쓰면 33, 3 + 3, 3 - 3, 3 × 3, 3 ÷ 3을 만듭니다. 세 번 쓴 수는 한 번 쓴 수와 두 번 쓴 수를 어떻게 조합해 만들까요?

## 🧪 예제 이해하기

N = 3, number = 4이면 한 번으로는 {3}, 두 번으로는 {33, 6, 0, 9, 1}을 만듭니다. 세 번이면 3 + 1 = 4를 만들 수 있어 결과는 3입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

made[k]는 N을 정확히 k번 써서 만들 수 있는 수의 집합입니다. N을 k번 이어 붙인 수를 넣고, k를 left_count + right_count로 나누는 방법마다 두 집합의 수를 사칙연산으로 합칩니다. number가 들어 있으면 k가 답입니다.

### 🐍 Python 코드

```python
def solution(N, number):
    made = [set()]
    for count in range(1, 9):
        current = set()
        current.add(int(str(N) * count))
        for left_count in range(1, count):
            right_count = count - left_count
            for left in made[left_count]:
                for right in made[right_count]:
                    current.add(left + right)
                    current.add(left - right)
                    current.add(left * right)
                    if right != 0:
                        current.add(left // right)
        if number in current:
            return count
        made.append(current)
    return -1
```

### 📖 코드 해설

made[0]은 비워 두어 made[k]가 정확히 k번 사용을 뜻하게 했습니다. str(N) * count는 문자열을 count번 이어 붙이고 int()로 숫자로 바꿉니다. 괄호를 어떻게 치든 마지막 연산 하나를 기준으로 왼쪽 식과 오른쪽 식으로 나눌 수 있습니다. 그래서 두 집합의 모든 짝을 사칙연산으로 합치면 k번 쓴 모든 수가 나옵니다. 빼기와 나누기는 순서가 중요해 (1, 2)와 (2, 1)을 둘 다 봅니다. 0으로 나누지 않도록 확인합니다.

같은 수가 여러 방법으로 만들어져도 집합에는 하나만 남아 계산량이 줄어듭니다.

### ⏱️ 시간 복잡도

made[k]의 크기를 S_k라 하면 k번째 단계의 연산 수는 a + b = k인 모든 짝의 S_a × S_b를 더한 값입니다. 계산량은 N과 number의 크기보다 집합의 크기가 정합니다. 사용 횟수가 8번까지라 집합이 끝없이 커지지는 않습니다.

### 💾 공간 복잡도

여덟 개의 집합 크기를 모두 더한 만큼 저장합니다.

## ⚠️ 실수하기 쉬운 점

- 55, 555처럼 이어 붙인 수를 빼먹기 쉽습니다.
- 앞 단계의 결과에 N 하나만 붙여 계산하면 (1회 + 1회) × (1회 + 1회) 같은 조합을 놓칩니다.
- Python의 //는 음수에서 아래쪽 정수로 내립니다. 예를 들어 -7 // 2는 -4입니다. 이 풀이는 //를 그대로 썼고 음수 나눗셈을 문제와 같은 방식으로 처리하는지는 공식 채점으로 확인해야 합니다.

## ✅ 배운 것

결과를 사용 횟수로 나눠 저장하면 작은 횟수의 결과를 조합해 큰 횟수의 결과를 만들 수 있습니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] number가 N과 같은 경우와 이어 붙인 수인 경우 확인하기

## 🚀 이어 풀어 볼 문제

- [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) (`43165`) — 연산 선택으로 목표 수를 만드는 탐색을 복습합니다.
- [거스름돈](https://school.programmers.co.kr/learn/courses/30/lessons/12907) (`12907`) — 작은 결과를 조합해 큰 결과를 만드는 DP를 비교합니다.
