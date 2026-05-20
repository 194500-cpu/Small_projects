import sys
import collections

rows, columns = map(int, sys.stdin.readline().strip().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(rows)]
backtracker = [[None] * columns for _ in range(rows)]
path = []
directions = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]
found = False
end = ()
current_row = 0
current_column = 0

for row in range(rows):
    for column in range(columns):
        if grid[row][column] == "A":
            start_row, start_column = row, column
            grid[row][column] = "#"
        elif grid[row][column] == "B":
            end_row, end_column = row, column

queue = collections.deque([(start_row, start_column)])

while queue:

    current_row, current_column = queue.popleft()
    if current_row == end_row and current_column == end_column:
        found = True
        break

    else:
        for direction_row, direction_column, notation in directions:
            new_row, new_column = current_row + direction_row, current_column + direction_column
            if  -1 < new_row < rows and -1 < new_column < columns:
                if grid[new_row][new_column] != "#":
                    backtracker[new_row][new_column] = (current_row, current_column, notation)
                    if grid[new_row][new_column] != "B":
                        grid[new_row][new_column] = "#"
                    queue.append((new_row, new_column))

if not found:
    print("NO")
else:
    print("YES")
    while end_row != start_row or end_column != start_column:
        previous_row, previous_column, notation = backtracker[end_row][end_column]
        path.append(notation)

        end_row, end_column = previous_row, previous_column
    path.reverse()
    print(len(path))
    print(*path, sep='')