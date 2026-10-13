# 🧩 행렬의 곱셈

- Programmers ID: 12949
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/12949
- Level: 2
- Stage: Level 2 Core 29
- Prerequisites: Level 1 내적, 2차원 인덱싱
- Core concepts: 행과 열의 내적, 세 중첩 반복

## 🎯 이 문제에서 배우는 것

같은 계산을 결과의 각 행과 열에 적용합니다.

## 🔎 문제 핵심

곱할 수 있는 두 행렬 arr1, arr2의 곱을 2차원 리스트로 돌려줍니다. 첫 행렬의 열 수와 두 번째 행렬의 행 수는 같습니다.

## 💭 먼저 생각해 보기

첫 행렬의 한 행과 두 번째 행렬의 한 열을 골라 위아래로 적고 같은 위치끼리 곱해 보세요.

## 🧪 예제 이해하기

arr1 = [[2,0],[1,3]], arr2 = [[1,4],[2,1]]이면 결과는 [[2,8],[7,7]]입니다. 왼쪽 아래는 1×1 + 3×2 = 7입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

결과의 행과 열을 정하고 그 칸에 필요한 내적을 계산합니다. 결과 크기는 첫 행렬의 행 수 × 두 번째 행렬의 열 수입니다.

### 🐍 Python 코드

```python
def solution(arr1, arr2):
    rows = len(arr1)
    shared = len(arr2)
    columns = len(arr2[0])
    result = []
    for row in range(rows):
        result_row = []
        for column in range(columns):
            total = 0
            for index in range(shared):
                total += arr1[row][index] * arr2[index][column]
            result_row.append(total)
        result.append(result_row)
    return result
```

### 📖 코드 해설

arr1[row][index]로 첫 행렬의 행을, arr2[index][column]으로 두 번째 행렬의 열을 읽습니다. 한 칸의 내적을 끝내면 그 값을 결과 행에 추가합니다. 결과 행마다 새 리스트를 만들어 독립적인 행으로 저장합니다. 같은 자리 두 수만 곱하는 계산은 행렬 곱셈과 다릅니다.

### ⏱️ 시간 복잡도

첫 행렬의 행 수 R, 공통 안쪽 길이 K, 두 번째 행렬의 열 수 C라 하면 결과 RC칸마다 K번 계산해 O(RKC)입니다.

### 💾 공간 복잡도

반환 행렬 RC칸을 새로 만듭니다. 반환값 포함 추가 공간은 O(RC), 반환값 제외 작업 변수의 공간은 O(1)입니다.

## ⚠️ 실수하기 쉬운 점

- 두 번째 행렬에서도 같은 행만 읽으면 내적이 아니라 다른 계산이 됩니다.
- 첫 행렬의 열 수와 두 번째 행렬의 행 수가 맞아야 합니다.

## ✅ 배운 것

결과의 한 칸은 첫 행렬의 한 행과 두 번째 행렬의 한 열을 곱해 더한 값입니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 정사각형이 아닌 행렬의 결과 크기 설명하기

## 🚀 이어 풀어 볼 문제

- [땅따먹기](https://school.programmers.co.kr/learn/courses/30/lessons/12913) (`12913`) — 2차원 리스트의 행과 열을 읽습니다.
- [연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701) (`131701`) — 반복할 때 같은 합계를 다시 계산하지 않는 방법을 봅니다.
