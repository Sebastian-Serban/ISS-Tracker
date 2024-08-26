maze = [
    "E..W*.W....",
    "..WW...W...",
    "..WWWW.WW..",
    ".......W...",
    "WW..W...W..",
    "..W....WW.W",
    ".W.WW..W...",
    "W...W...WW.",
    ".WW...W....",
    ".....WW...."
]


def find_path_with_moves(maze, target_moves):
    rows, cols = len(maze), len(maze[0])

    maze_matrix = [list(row) for row in maze]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid_move(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze_matrix[x][y] in ('.', 'E', '*')

    def bfs(start_x, start_y):
        queue = [(start_x, start_y, [(start_x, start_y)])]
        visited = set((start_x, start_y))

        while queue:
            x, y, path = queue.pop(0)
            if maze_matrix[x][y] == '*' and len(path) == target_moves + 1:
                return path

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and is_valid_move(nx, ny):
                    visited.add((nx, ny))
                    new_path = path + [(nx, ny)]
                    queue.append((nx, ny, new_path))

        return []

    start_pos = [(i, row.index('E')) for i, row in enumerate(maze) if 'E' in row][0]
    path = bfs(start_pos[0], start_pos[1])

    if len(path) == target_moves + 1:
        for x, y in path[1:]:
            if maze_matrix[x][y] == '.':
                maze_matrix[x][y] = 'P'
        return "\n".join([' '.join(row) for row in maze_matrix]), len(path) - 1  # Subtract 1 for the start position
    else:
        return ["No path found with {} moves".format(target_moves)], 0

# Finding a path with 23 moves
print(find_path_with_moves(maze, 14)[0])
