
def q1_solution(bugseq: list[list[int]]):
    print(bugseq)
    return f(bugseq, 0)

def f(bugseq, start_time: int) -> int:
    max_bug = 0
    for i in range(len(bugseq)):
        t, limit = bugseq[i]
        if start_time + t <= limit:
            res = 1 + f(bugseq[:i] + bugseq[i+1:], start_time + t)
            max_bug = max(max_bug, res)

    return max_bug
