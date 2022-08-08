import sys
input = sys.stdin.readline


def find_parent(x, p):
    if p[x] != x:
        p[x] = find_parent(p[x], p)
    return p[x]


def solution(n, costs):
    answer = 0
    possible_route = [[i] for i in range(n)]
    parent = [i for i in range(n)]
    for left, right, cost in sorted(costs, key=lambda x: x[2]):
        left_parent = find_parent(left, parent)
        right_parent = find_parent(right, parent)
        if left_parent == right_parent:
            continue
        else:
            min_parent, max_parent = min(left_parent, right_parent), max(left_parent, right_parent)
            possible_route[min_parent] += possible_route[max_parent]
            parent[max_parent] = min_parent
            answer += cost

        if len(possible_route[0]) == n:
            break

    return answer