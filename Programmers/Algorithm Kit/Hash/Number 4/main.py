from collections import defaultdict

def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    n = len(plays)
    for i in range(n):
        dic[genres[i]].append((plays[i], i))

    genre_list = sorted(dic.keys(), key=lambda x: sum([song[0] for song in dic[x]]), reverse=True)
    for genre in genre_list:
        song_list = sorted(dic[genre], key=lambda x: x[0], reverse=True)
        answer += [song[1] for song in song_list[:2]]

    return answer