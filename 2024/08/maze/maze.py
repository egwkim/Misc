import random


def rand_dfs(x, y):
    # 0: shaft, 1: wall
    maze = [2 ** (2 * x + 1) - 1] * (2 * y + 1)

    visited = [[False] * x for _ in range(y)]
    cur = (0, 0)
    cur_x, cur_y = cur
    stack = [cur]
    visited[0][0] = True
    maze[0] -= 1 << 1
    maze[1] -= 1 << 1
    maze[-1] -= 1 << 2 * x - 1

    for i in range(x * y - 1):
        while True:
            neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for j in (3, 2, 1, 0):
                dx, dy = neighbors[j]
                # check index out of range
                if (cur_x + dx) == -1 or (cur_y + dy) == -1:
                    neighbors.pop(j)
                elif (cur_x + dx) == x or (cur_y + dy) == y:
                    neighbors.pop(j)

                # check visited
                elif visited[cur_y + dy][cur_x + dx]:
                    neighbors.pop(j)
            if len(neighbors) == 0:
                cur = stack.pop()
                cur_x, cur_y = cur
            else:
                break

        stack.append(cur)
        dx, dy = neighbors[random.randrange(len(neighbors))]
        maze[2 * cur_y + 1 + dy] -= 1 << 2 * cur_x + 1 + dx
        cur = (cur_x + dx, cur_y + dy)
        cur_x, cur_y = cur
        maze[2 * cur_y + 1] -= 1 << 2 * cur_x + 1
        visited[cur_y][cur_x] = True

    maze_str = '\n'.join(f'{row:b}'[::-1] for row in maze)
    maze_str = maze_str.replace('0', '  ')
    maze_str = maze_str.replace('1', '██')
    return maze_str


def main():
    x, y = map(int, input().split())
    maze = rand_dfs(x, y)
    with open('maze.txt', 'w', encoding='utf-8') as f:
        f.write(maze)


if __name__ == "__main__":
    main()
