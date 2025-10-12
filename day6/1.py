'''
URL: https://adventofcode.com/2024/day/6
answer = 4696
'''

def cal_guard_tour(grid, directions, position):
    h, w = len(grid), len(grid[0])

    visited = set([position])       
    grid[position[0]][position[1]] = 'X' 
    direction = 0

    while True:
        dy, dx = directions[direction]
        ny, nx = position[0] + dy, position[1] + dx

        if not (0 <= ny < h and 0 <= nx < w):
            break

        if grid[ny][nx] == '#':
            direction = (direction + 1) % len(directions)
            continue

        position = (ny, nx)
        if position not in visited:
            visited.add(position)
            grid[ny][nx] = 'X'

    return len(visited)

def main():
    with open("input.txt", "r") as f:
        map_area = [list(line.strip()) for line in f.readlines()]

    
    position = next(( (i, j) for i, fila in enumerate(map_area) for j, c in enumerate(fila) if c == '^' ), None)
    directions = [(-1,0), (0,1), (1,0), (0,-1)] # up - right, down, left
    print(cal_guard_tour(map_area, directions, position))

if __name__ == "__main__":
    main()