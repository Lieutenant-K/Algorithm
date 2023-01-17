from collections import deque
def solution(begin, target, words):
    dic = dict(zip(words, [0]*len(words)))
    dic[begin] = dic[target] = 0
    queue = deque([begin])
    while queue:
        now = queue.popleft()
        for word in words:
            if not dic[word] and len([i for i in range(len(word)) if now[i] != word[i]]) == 1:
                dic[word] = dic[now] + 1
                queue.append(word)
    return dic[target]
