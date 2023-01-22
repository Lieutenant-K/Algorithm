from collections import defaultdict
def dfs(route, tickets, answer):
    if sum([len(array) for array in tickets.values()]) == 0:
        answer.append(route)
    current = route[-1]
    remain = tickets[current]
    for i in range(len(remain)):
        dic = tickets.copy()
        dic[current] = remain[:i] + remain[i+1:]
        dfs(route+[remain[i]], dic, answer)

def solution(tickets):
    dic, answer = defaultdict(list), []
    for start, end in sorted(tickets):
        dic[start].append(end)
    dfs(["ICN"], dic, answer)
    return answer[0]
