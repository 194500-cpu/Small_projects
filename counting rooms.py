import collections
import sys

rows, columns = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for line in range(rows)]
rooms = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for row in range(rows):
    for column in range(columns):
        if grid[row][column] == '.':
            rooms += 1

            queue = collections.deque([(row, column)])
            grid[row][column] = '#'

            while len(queue) != 0:
                current_row, current_column = queue.popleft()
                for update_row, update_column in directions:
                    new_row = current_row + update_row
                    new_column = current_column + update_column

                    if -1 < new_row < rows and -1 < new_column < columns:
                        if grid[new_row][new_column] == ".":
                            grid[new_row][new_column] = "#"
                            queue.append((new_row, new_column))

print(rooms)