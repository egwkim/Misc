import random
import struct


def bmp(maze):
    maze_width = maze[0].bit_length()
    maze_height = len(maze)

    cell_size = 1

    # maze_width * cell_size pixel per row
    # maze_width * cell_size bits per row
    # maze_width * cell_size + 7 // 8 bytes per row
    # ((maze_width * cell_size + 7 // 8) + 3) // 4
    row_size = 4 * (((maze_width * cell_size + 7) // 8 + 3) // 4)

    BMP_HEADER_SIZE = 14
    DIB_HEADER_SIZE = 40
    PALLETE_SIZE = 4 * 2
    BMP_DATA_SIZE = row_size * maze_height * cell_size
    FILE_SIZE = BMP_HEADER_SIZE + DIB_HEADER_SIZE + PALLETE_SIZE + BMP_DATA_SIZE

    # Bitmap file header
    data = b'BM'  # ID
    data += struct.pack('<I', FILE_SIZE)  # File size
    data += struct.pack('<h', 0)  # Unused
    data += struct.pack('<h', 0)  # Unused
    data += struct.pack('<I', FILE_SIZE - BMP_DATA_SIZE)  # Start of bitmap data

    # DIB header (BITMAPINFOHEADER)
    data += struct.pack('<I', 40)  # DIB header size
    data += struct.pack('<I', maze_width * cell_size)  # Image width
    data += struct.pack('<I', maze_height * cell_size)  # Image height
    data += struct.pack('<h', 1)  # Number of color planes
    data += struct.pack('<h', 1)  # Bits per pixel
    data += struct.pack('<I', 0)  # Compression method
    data += struct.pack('<I', BMP_DATA_SIZE)  # Size of bitmap data
    data += struct.pack('<I', 3780)  # Horizontal resolution, pixel per meter
    data += struct.pack('<I', 3780)  # Vertical resolution, pixel per meter
    data += struct.pack('<I', 2)  # Number of colors in the color pallete
    data += struct.pack('<I', 0)  # Number of important colors

    # Color pallete
    data += bytearray.fromhex('FFFFFF00')  # White
    data += bytearray.fromhex('00000000')  # Black

    # Bitmap data
    for row in maze[::-1]:
        maze_data = 0
        walls = (1 << cell_size) - 1
        for _ in range(maze_width):
            if row & 1:
                maze_data += walls
            walls <<= cell_size
            row >>= 1
        maze_data <<= row_size * 8 - cell_size * maze_width
        data += maze_data.to_bytes(row_size) * cell_size

    return data


def rand_dfs(w, h):
    # 0: shaft, 1: wall
    maze = [2 ** (2 * w + 1) - 1] * (2 * h + 1)

    visited = [[False] * w for _ in range(h)]

    # x, y interval is two cells
    cur = (0, 0)
    x, y = cur
    stack = [cur]
    visited[0][0] = True
    maze[0] -= 1 << 2 * w - 1
    maze[1] -= 1 << 2 * w - 1
    maze[-1] -= 1 << 1

    for i in range(w * h - 1):
        while True:
            neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for j in (3, 2, 1, 0):
                dx, dy = neighbors[j]
                # check index out of range
                if (x + dx) == -1 or (y + dy) == -1:
                    neighbors.pop(j)
                elif (x + dx) == w or (y + dy) == h:
                    neighbors.pop(j)

                # check visited
                elif visited[y + dy][x + dx]:
                    neighbors.pop(j)
            if len(neighbors) == 0:
                cur = stack.pop()
                x, y = cur
            else:
                break

        stack.append(cur)
        dx, dy = neighbors[random.randrange(len(neighbors))]
        maze[2 * y + 1 + dy] -= 1 << 2 * w - (2 * x + 1 + dx)
        cur = (x + dx, y + dy)
        x, y = cur
        maze[2 * y + 1] -= 1 << 2 * w - (2 * x + 1)
        visited[y][x] = True

    return maze


def maze_str(maze):
    maze_str = '\n'.join(f'{row:b}' for row in maze)
    maze_str = maze_str.replace('0', '  ')
    maze_str = maze_str.replace('1', '██')
    return maze_str


def main():
    w, h = map(int, input().split())

    maze = rand_dfs(w, h)
    # with open('maze.txt', 'w', encoding='utf-8') as f:
    #     f.write(maze_str(maze))

    maze_data = bmp(maze)
    with open('maze.bmp', 'wb') as f:
        f.write(maze_data)


if __name__ == "__main__":
    main()
