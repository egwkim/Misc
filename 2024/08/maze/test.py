import maze
import solve

m = maze.rand_dfs(10, 10)
m_ = solve.decode_maze_str(maze.maze_str(m))

assert m == m_

print(maze.maze_str(m))
s = solve.dfs(m)
print(s)
print(solve.maze_str_with_sol(m, s))

# with open('maze.bmp', 'rb') as f:
#     data = f.read()

# decoded = solve.decode_bmp(data)
# print(maze.maze_str(decoded))
# s = solve.dfs(decoded)
# data = solve.bmp_with_sol(decoded, s)
# with open('maze_solved.bmp', 'wb') as f:
#     f.write(data)
