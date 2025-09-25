'''
    URL: https://adventofcode.com/2024/day/3
    answer: 161289189
'''
import re

PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def process_line(line):
    line = line.strip()
    line_split = PATTERN.findall(line)
    mul_calculation = sum([int(x)* int(y) for x, y in line_split])
    return mul_calculation

def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    result_per_line = []
    for i in lines:
        result_per_line.append(process_line(i))

    answer = sum(result_per_line)
    print(answer) 

if __name__ == "__main__":
    main()