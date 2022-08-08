from collections import deque
from collections import defaultdict
def solution(begin, target, words):
    visit, count = defaultdict(bool), defaultdict(int)
    visit[begin] = True
    queue = deque([begin])
    while queue:
        word = queue.popleft()
        if word == target:
            return count[word]
        for w in words:
            if not visit[w] and sum([int(w[i] != word[i]) for i in range(len(w))]) == 1:
                visit[w] = True
                count[w] = count[word]+1
                queue.append(w)
    return 0