from collections import deque

glob_max = 0

def q3_solution(time: list, prerequisites: list[tuple]):
    n = len(time)
    adj = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]
    Q = deque()

    for pre in prerequisites:
        adj[pre[1] - 1].append(pre[0] - 1)
        indegree[pre[0] - 1] += 1

    total_max = 0
    print(adj)
    for i in range(n):
        if indegree[i] == 0:
            Q.append(i)
            cost = dfs(adj, time, [False for _ in range(n)], i)
            total_max = max(total_max, cost)

    return total_max

    # res = 0
    # while Q:
    #     level_size = len(Q)
    #     level_res = 0
    #     for _ in range(level_size):
    #         cur = Q.popleft()
    #         level_res = max(level_res, time[cur])
    #         for ngbr in adj[cur]:
    #             indegree[ngbr] -= 1
    #             if indegree[ngbr] == 0:
    #                 Q.append(ngbr)
    #     res += level_res


def dfs(adj, time, visited, i):
    if len(adj[i]) == 0:
        return time[i]

    max_cost = 0
    for ngbr in adj[i]:
        # if ngbr not in visited:
            visited[ngbr] = True
            ngbr_cost = dfs(adj, time, visited, ngbr)
            max_cost = max(max_cost, time[i] + ngbr_cost)

    return max_cost