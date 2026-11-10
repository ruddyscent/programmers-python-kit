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
