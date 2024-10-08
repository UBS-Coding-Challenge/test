from collections import deque
from pprint import pprint
from copy import deepcopy
import copy

direction_move = {
    'u': (-1, 0),
    'd': (1, 0),
    'r': (0, 1),
    'l': (0, -1)
}

res = []

def q2_solution(grid: list[list[str]]):
    m, n = len(grid), len(grid[0])
    timelapse = [[set() for _ in range(n)] for _ in range(m)]
    bullet_map = [[set() for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] in ['u', 'd', 'r', 'l']:
                bullet_map[i][j].add(grid[i][j])
                mark_time(grid, timelapse, i, j, grid[i][j])

    # for t in timelapse:
    #     print(t)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                f(grid, timelapse, bullet_map, i, j, [], 0)

    return res

def get_timelapse_list(timelapse_list):
    return [x[0] for x in list(timelapse_list)]

def exist_target(timelapse_list, time, d):
    for x, y in list(timelapse_list):
        if (time == x) and d == y:
            return True
    return False

def f(grid, timelapse, bullet_map, i, j, path, cur_time):
    m, n = len(grid), len(grid[0])
    if i < 0 or i >= m or j < 0 or j >= n:
        return

    all_greater = True
    for btime in get_timelapse_list(timelapse[i][j]):
        if cur_time <= btime:
            all_greater = False
            break

    if all_greater and grid[i][j] != '*':
        global res
        res = path[:]
        return

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    at_least_one_pass = False

    before_cur_time = cur_time if cur_time == 0 else cur_time - 1
    # print(moved_bullet_map)
    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        break_flag = False
        for btime in get_timelapse_list(timelapse[nx][ny]):
            if cur_time + 1 == btime:
                break_flag = True
                break
        if break_flag:
            continue

        # if nx == 3 and ny == 2 and d == 3:
        #     print("sdf")

        direction = None
        if d == 0: # down
            direction = 'd'
            if exist_target(timelapse[nx][ny], cur_time, 'u'):
                continue
        elif d == 1: # right
            direction = 'r'
            if exist_target(timelapse[nx][ny], cur_time, 'l'):
                continue
        elif d == 2: # up
            direction = 'u'
            if exist_target(timelapse[nx][ny], cur_time, 'd'):
                continue
        else: # left
            direction = 'l'
            if exist_target(timelapse[nx][ny], cur_time, 'r'):
                continue

        at_least_one_pass = True
        f(grid, timelapse, None, nx, ny, path + [direction], cur_time + 1)

    if not at_least_one_pass:
        return


def mark_time(grid, timelapse, i, j, direction):
    m, n = len(grid), len(grid[0])
    dx, dy = direction_move[direction]
    cnt = 0

    while i >= 0 and j >= 0 and i < m and j < n:
        # print(i, j)
        timelapse[i][j].add((cnt, direction))
        i, j = i + dx, j + dy
        cnt += 1

def move_map(grid, bullet_map):
    temp_bullet_map = copy.deepcopy(bullet_map)
    # pprint(temp_bullet_map)
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            for bullet_type in list(bullet_map[i][j]):
                move(grid, temp_bullet_map, i, j, bullet_type)
    # pprint(temp_bullet_map)
    # print("-" * 100)
    return temp_bullet_map

def move(grid, bullet_map, i, j, bullet_type):
    m, n = len(grid), len(grid[0])
    dx, dy = direction_move[bullet_type]

    nx, ny = i + dx, j + dy
    if nx < 0 or nx >= m or ny < 0 or ny >= n:
        return
    bullet_map[i][j].remove(bullet_type)
    bullet_map[nx][ny].add(bullet_type)

