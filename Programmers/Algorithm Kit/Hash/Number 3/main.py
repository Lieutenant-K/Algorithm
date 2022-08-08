from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(list)
    for name, parts in clothes:
        dic[parts].append(name)

    for parts in dic.keys():
        answer *= len(dic[parts]) + 1

    return answer - 1