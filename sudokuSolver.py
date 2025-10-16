grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_valid(grid, r, c, k):
    not_in_row = k not in [grid[r][i] for i in range(9)]
    not_in_column = k not in [grid[i][c] for i in range(9)]
    subgrid = [[grid[j][i] for i in range((c // 3) * 3, ((c // 3) * 3) + 3)] for j in range((r // 3) * 3, ((r // 3) * 3) + 3)]
    not_in_subgrid = True
    for list in subgrid:
        if k in list:
            not_in_subgrid = False
            break


    if not_in_row and not_in_column and not_in_subgrid:
        return True
    else:
        return False

def backtracking(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in nums:
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if backtracking(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

if backtracking(grid):
    for row in grid:
        print(row)
else:
    print("Sem solução")