"""
Description

There is a ball is placed on a maze with empty spaces and walls.
The ball can go through empty spaces by tilting up, down, left or right, but it won't stop rolling until hitting a wall.
When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze,
find the shortest amount of moves for the ball to stop at the destination.
A move is defined as tilting up, down, left or right and the ball rolling that direction until it hits a wall.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space.
You may assume that the borders of the maze are all walls.
The start and destination coordinates are represented by row and column indexes.
"""

from collections import deque


def tiltMaze(maze, source, goal):
    nmoves = tiltMazeBFS(maze, source, goal)
    return nmoves


def tiltMazeBFS(maze, source, goal):
    if source == goal:
        return 0

    queue = deque([source])
    nmoves = 0
    visited = set()

    # BFS layer by layer
    while queue:
        next_positions = deque([])
        for _ in range(len(queue)):
            curr_x, curr_y = queue.popleft()
            visited.add((curr_x, curr_y))
            if curr_x == goal[0] and curr_y == goal[1]:
                return nmoves
            curr_x_l, curr_y_l = goleft(maze, [curr_x, curr_y])
            if (curr_x_l, curr_y_l) not in visited:
                next_positions.append([curr_x_l, curr_y_l])
            curr_x_r, curr_y_r = goright(maze, [curr_x, curr_y])
            if (curr_x_r, curr_y_r) not in visited:
                next_positions.append([curr_x_r, curr_y_r])
            curr_x_u, curr_y_u = goup(maze, [curr_x, curr_y])
            if (curr_x_u, curr_y_u) not in visited:
                next_positions.append([curr_x_u, curr_y_u])
            curr_x_d, curr_y_d = godown(maze, [curr_x, curr_y])
            if (curr_x_d, curr_y_d) not in visited:
                next_positions.append([curr_x_d, curr_y_d])
        queue = next_positions
        nmoves += 1
    return -1


def goleft(maze, source):
    row, col = source[0], source[1]
    while col >= 0 and maze[row][col] != 1:
        col -= 1
    return row, col + 1


def goright(maze, source):
    row, col = source[0], source[1]
    while col < len(maze[0]) and maze[row][col] != 1:
        col += 1
    return row, col - 1


def goup(maze, source):
    row, col = source[0], source[1]
    while row >= 0 and maze[row][col] != 1:
        row -= 1
    return row + 1, col


def godown(maze, source):
    row, col = source[0], source[1]
    while row < len(maze) and maze[row][col] != 1:
        row += 1
    return row - 1, col


maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
goal = [4, 4]
print(tiltMaze(maze, start, goal))

