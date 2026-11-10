# 🧩 베스트앨범

- Programmers ID: 42579
- Official link: https://school.programmers.co.kr/learn/courses/30/lessons/42579
- Level: 3
- Stage: Level 3 Core 01
- Prerequisites: Level 2 09 딕셔너리, Level 1 20 정렬 기준 함수, 튜플
- Core concepts: 딕셔너리로 묶기, 여러 기준 정렬

## 🎯 이 문제에서 배우는 것

같은 종류끼리 모은 뒤 두 단계의 정렬 기준으로 순서를 정합니다.

## 🔎 문제 핵심

노래마다 장르와 재생 수가 있고 노래 번호는 리스트 위치입니다. 총 재생 수가 많은 장르부터, 장르 안에서는 재생 수가 많은 노래부터 최대 두 곡씩 고릅니다. 재생 수가 같으면 번호가 작은 노래가 먼저입니다. 고른 노래 번호를 순서대로 돌려줍니다.

## 💭 먼저 생각해 보기

장르별 총 재생 수와 장르별 노래 목록은 각각 무엇을 키로 저장하면 될까요? 장르 안에서 재생 수가 같은 두 곡은 어떻게 줄 세우나요?

## 🧪 예제 이해하기

genres가 ["rock", "jazz", "rock", "rock"], plays가 [100, 300, 200, 100]이라고 합시다. rock은 400, jazz는 300이라 rock이 먼저입니다. rock 노래는 2번(200), 0번(100), 3번(100) 순서이고 앞의 두 곡만 고릅니다. 이어서 jazz의 1번을 넣어 결과는 [2, 0, 1]입니다.

## 🛠️ 풀이 1. 이해하기 쉬운 방법

### 💡 아이디어

한 번 순회하며 장르별 총합과 (재생 수, 번호) 목록을 만듭니다. 장르는 총합이 큰 순서로, 노래는 재생 수가 큰 순서와 번호가 작은 순서로 정렬해 앞의 두 곡을 담습니다.

### 🐍 Python 코드

```python
def solution(genres, plays):
    genre_totals = {}
    genre_songs = {}
    for song_id in range(len(genres)):
        genre = genres[song_id]
        play = plays[song_id]
        genre_totals[genre] = genre_totals.get(genre, 0) + play
        if genre not in genre_songs:
            genre_songs[genre] = []
        genre_songs[genre].append((play, song_id))

    def genre_key(genre):
        return genre_totals[genre]

    def song_key(song):
        play, song_id = song
        return (-play, song_id)

    album = []
    for genre in sorted(genre_totals, key=genre_key, reverse=True):
        songs = sorted(genre_songs[genre], key=song_key)
        for play, song_id in songs[:2]:
            album.append(song_id)
    return album
```

### 📖 코드 해설

genre_totals는 장르를 키로 총 재생 수를, genre_songs는 장르를 키로 노래 목록을 저장합니다. sorted(genre_totals, ...)처럼 딕셔너리를 정렬하면 키들이 정렬됩니다. song_key는 (-play, song_id)를 돌려줍니다. 튜플은 앞의 값부터 비교하므로 재생 수가 큰 노래가 먼저 오고 재생 수가 같으면 번호가 작은 노래가 먼저 옵니다. 재생 수에 -를 붙여 큰 값을 앞으로 보냈습니다. songs[:2]는 곡이 하나뿐이면 그 한 곡만 꺼냅니다.

```text
rock -> [(100, 0), (200, 2), (100, 3)]
정렬  -> [(200, 2), (100, 0), (100, 3)]
          앞의 두 곡 선택: 2, 0
```

### ⏱️ 시간 복잡도

노래 수를 N, 장르 수를 G라 합니다. 묶는 데 평균 O(N), 장르 정렬에 O(G log G)가 걸립니다. 장르별 노래 정렬을 모두 합하면 O(N log N)을 넘지 않아 전체 O(N log N)입니다. 장르 이름의 해시 계산은 이름 길이가 짧아 한 번의 연산으로 셉니다.

### 💾 공간 복잡도

장르별 총합과 노래 목록, 정렬로 만든 새 리스트에 O(N)을 씁니다. 반환값은 최대 2G개라 전체 추가 공간은 O(N)입니다.

## ⚠️ 실수하기 쉬운 점

- 장르 순서는 노래 수가 아니라 총 재생 수로 정합니다.
- 장르에 곡이 하나뿐이면 한 곡만 넣습니다.
- 재생 수가 같을 때 번호가 작은 노래를 먼저 고릅니다.

## ✅ 배운 것

딕셔너리로 묶은 뒤 튜플 정렬 기준으로 여러 조건을 한 번에 표현합니다.

## 🔁 다시 풀어보기

- [ ] 프로그래머스에서 직접 작성한 코드로 채점 통과하기
- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법과 알고리즘을 선택한 이유 설명하기
- [ ] 곡이 하나인 장르와 재생 수가 같은 노래가 있는 예를 만들어 확인하기

## 🚀 이어 풀어 볼 문제

- [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578) (`42578`) — 딕셔너리로 종류별 자료를 모으는 연습을 복습합니다.
- [다단계 칫솔 판매](https://school.programmers.co.kr/learn/courses/30/lessons/77486) (`77486`) — 이름을 키로 사람 사이의 관계를 저장합니다.
