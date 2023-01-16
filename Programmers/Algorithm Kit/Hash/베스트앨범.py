from collections import defaultdict
def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    for i in range(len(genres)):
        dic[genres[i]].append((i, plays[i]))
    for song_list in sorted(dic.values(), key=lambda list: sum(map(lambda x: x[1], list)), reverse=True):
        answer += list(map(lambda x: x[0], sorted(sorted(song_list), key=lambda x: x[1], reverse=True)))[:2]
    return answer
