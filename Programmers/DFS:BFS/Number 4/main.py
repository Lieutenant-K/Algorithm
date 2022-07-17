def dfs(airport, route, remain_tickets, result):
    if len(remain_tickets) == 0:
        result.append(route)
    for start, end in remain_tickets:
        if airport == start:
            rt = remain_tickets[:]
            rt.remove([start, end])
            path = route[:]
            path.append(end)
            dfs(end, path, rt, result)

def solution(tickets):
    answer = []
    dfs("ICN", ["ICN"], tickets, answer)
    answer.sort()
    return answer[0]