
def q1_solution(bugseq: list[list[int]]):
    return f(bugseq, 0)

def f(bugseq: list[list[int]], start_time: int) -> int:
    if len(bugseq) == 0:
        return 0

    max_bug = 0
    for i in range(len(bugseq)):
        t, limit = bugseq[i]
        if start_time + t <= limit:
            res = 1 + f(bugseq[:i] + bugseq[i+1:], start_time + t)
            max_bug = max(max_bug, res)

    return max_bug
