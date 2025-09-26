'''
    URL: https://adventofcode.com/2024/day/3#part2
    answer: 83595109

    This was my first solution, but it can be optimized by using re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")
    and then enabling or disabling a flag to determine whether or not to calculate it depending on whether a do() or don't() was encountered.

'''
import re

MUL_PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def process_line(line):
    line = line.strip()
    line_split = line.split("don't()")
    first_muls = MUL_PATTERN.findall(line_split[0])
    mul_calculation = sum([int(x)* int(y) for x, y in first_muls])
    for part in line_split[1:]:
        if len(part.split('do()')) >= 2:
            line_pattern = [MUL_PATTERN.findall(x) for x in part.split('do()')[1:]]
            mul_calculation += sum([int(x)* int(y) for line_cut in line_pattern for x, y in line_cut])

    return mul_calculation


def main():
    with open("input2.txt") as f:
        lines = f.read().splitlines()

    result_per_line = []
    for i in lines:
        result_per_line.append(process_line(i))

    answer = sum(result_per_line)
    print(answer) 

if __name__ == "__main__":
    main()