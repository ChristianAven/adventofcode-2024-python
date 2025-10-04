'''
URL: https://adventofcode.com/2024/day/4
answer = 2567

Is not necessary to use KMP algorithm because the word is short
'''

def find_words(grid, directions, word):
    lines = range(len(grid))
    cols_line = range(len(grid[0]))
    len_word = len(word)
    targets = [word, word[::-1]]
    count = 0

    for line in lines:
        for target in targets:
            count += grid[line].count(target)
        for col_line in cols_line:
            for target in targets:
                if grid[line][col_line] != target[0]:
                    continue
                for row_direction, col_direction in directions:
                    matches = True
                    for index_letter in range(1, len_word):
                        nr = line + row_direction * index_letter
                        nc = col_line + col_direction * index_letter
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                            if grid[nr][nc] != target[index_letter]:
                                matches = False
                                break
                        else:
                            matches = False
                            break
                    if matches:
                        count += 1
    return count

def main(word):
    with open("input.txt") as f:
        lines = f.read().splitlines()

    result = 0
    directions = [(1, 0), (1, 1), (1, -1)]  # down, down-right, down-left
    result = find_words(lines, directions, word)
    print(result)

if __name__ == "__main__":
    main("XMAS")