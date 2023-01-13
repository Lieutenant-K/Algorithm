def dfs(pre, x, graph):
    return 1+sum([dfs(x, node, graph) for node in graph[x] if node != pre])

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    return min([abs(dfs(a, b, graph)-dfs(b, a, graph)) for a, b in wires])
