from collections import deque
from typing import Tuple


def q10_klotski(board_str: str, moves: str) -> str:
    board = []
    for row in range(5):
        board.append(list(board_str[row * 4 : row * 4 + 4]))

    m, n = len(board), len(board[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    group = {}

    for i in range(m):
        for j in range(n):
            if not visited[i][j] and board[i][j] != '@':
                top_left, bottom_right = bfs(board, visited, i, j)
                group[board[i][j]] = (top_left, bottom_right)

    for i in range(0, len(moves), 2):
        target, direction = moves[i: i+2]
        move_block(board, group, target, direction)

    res = ""
    for i in range(m):
        for j in range(n):
            res += board[i][j]

    return res

def move_block(board: list[list[str]], group: dict, target: str, direction: str):
    if direction == 'E':
        move_east(board, group, target)
    elif direction == 'W':
        move_west(board, group, target)
    elif direction == 'S':
        move_south(board, group, target)
    else:
        move_north(board, group, target)

def move_east(board: list[list[str]], group: dict, target: str):
    top_left, bottom_right = group[target]
    x, y = top_left
    x_, y_ = bottom_right
    for i in range(x, x_ + 1):
        board[i][y_ + 1] = target
        board[i][y] = '@'

    group[target] = (x, y + 1), (x_, y_ + 1)

def move_west(board: list[list[str]], group: dict, target: str):
    top_left, bottom_right = group[target]
    x, y = top_left
    x_, y_ = bottom_right
    for i in range(x, x_ + 1):
        board[i][y_] = '@'
        board[i][y - 1] = target

    group[target] = (x, y - 1), (x_, y_ - 1)

def move_south(board: list[list[str]], group: dict, target: str):
    top_left, bottom_right = group[target]
    x, y = top_left
    x_, y_ = bottom_right
    for j in range(y, y_ + 1):
        board[x_ + 1][j] = target
        board[x][j] = '@'

    group[target] = (x + 1, y), (x_ + 1, y_)

def move_north(board: list[list[str]], group: dict, target: str):
    top_left, bottom_right = group[target]
    x, y = top_left
    x_, y_ = bottom_right
    for j in range(y, y_ + 1):
        board[x - 1][j] = target
        board[x_][j] = '@'

    group[target] = (x - 1, y), (x_ - 1, y_)


def bfs(board: list[str], visited: list[list[bool]], i: int, j: int) -> \
tuple[tuple[int, int], tuple[int, int]]:
    m, n = len(board), len(board[0])
    top_left = (i, j)
    bottom_right = (i, j)
    visited[i][j] = True
    Q = deque([(i, j)])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    c = board[i][j]

    while Q:
        cur = Q.popleft()
        for d in range(4):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] or board[nx][ny] == '@' or board[nx][ny] != c:
                continue

            visited[nx][ny] = True
            Q.append((nx, ny))
            if nx >= bottom_right[0] and ny >= bottom_right[1]:
                bottom_right = nx, ny

    return top_left, bottom_right





