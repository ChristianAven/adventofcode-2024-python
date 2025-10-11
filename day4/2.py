'''
URL: https://adventofcode.com/2024/day/4#part2
answer = 2029
'''

def count_x_mas(grid):
    R, C = len(grid), len(grid[0])
    cnt = 0
    for r in range(1, R - 1):
        for c in range(1, C - 1):
            if grid[r][c] != 'A':
                continue
            diag1 = grid[r - 1][c - 1] + grid[r + 1][c + 1]
            diag2 = grid[r - 1][c + 1] + grid[r + 1][c - 1]
            if (diag1 in ('MS', 'SM')) and (diag2 in ('MS', 'SM')):
                cnt += 1
    return cnt

def main():
    with open("input.txt") as f:
        grid = f.read().splitlines()
    print(count_x_mas(grid))

if __name__ == "__main__":
    main()