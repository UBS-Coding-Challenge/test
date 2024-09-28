
def q13_solution(generations: int, colony: str):
    dp = [[[-1 for _ in range(generations + 1)] for _ in range(10)] for _ in range(10)]
    n = len(colony)
    res = int(colony[-1])
    for i in range(n - 1):
        x, y = int(colony[i]), int(colony[i + 1])
        t = f(dp, x, y, generations)
        res += (t - y)
    return res


def f(dp, i, j, gens):
    if gens == 0:
        return i + j

    if dp[i][j][gens] != -1:
        return dp[i][j][gens]

    new_val = int(str(i + j + (i - j if i >= j else 10 - (j - i)))[-1])

    dp[i][j][gens] = f(dp, i, new_val, gens - 1) + f(dp, new_val, j, gens - 1) - new_val
    return dp[i][j][gens]

