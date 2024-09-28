from collections import deque

glob_max = 0

def q3_solution(time: list, prerequisites: list[tuple]):
    n = len(time)
    adj = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]
    Q = deque()

    for pre in prerequisites:
        adj[pre[0] - 1].append(pre[1] - 1)
        indegree[pre[1] - 1] += 1

    for i in range(n):
        if indegree[i] == 0:
            Q.append(i)
            print(i)
            dfs(adj, time, [False for _ in range(n)], i, time[i])

    return glob_max

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


def dfs(adj, time, visited, i, running_sum):
    if len(adj[i]) == 0:
        global glob_max
        glob_max = max(glob_max, running_sum)

    for ngbr in adj[i]:
        if ngbr not in visited:
            visited[ngbr] = True
            dfs(adj, time, visited, ngbr, running_sum + time[ngbr])