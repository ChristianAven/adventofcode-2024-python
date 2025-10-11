'''
URL: https://adventofcode.com/2024/day/5
answer = 6384
'''

from collections import defaultdict
from pathlib import Path


def parse_input(path):
    text = Path(path).read_text().splitlines()
    sep = text.index("")
    raw_rules = text[:sep]
    raw_pages = text[sep + 1:]

    rules = [tuple(line.split("|")) for line in raw_rules]
    pages = [line.split(",") for line in raw_pages]
    return rules, pages

def get_rules(rules):
    rule_map = {}
    for a, b in rules:
        if a not in rule_map:
            rule_map[a] = set()
        rule_map[a].add(b)
    return rule_map

def page_is_valid(page, rule_map):
    pos = {v: i for i, v in enumerate(page)}
    for a, successors in rule_map.items():
        if a not in pos:
            continue
        pa = pos[a]
        for b in successors:
            pb = pos.get(b)
            if pb is not None and pa > pb:
                return False
    return True


def sum_middle_of_valid_pages(rule_map, pages):
    total = 0
    for page in pages:
        if page_is_valid(page, rule_map):
            total += int(page[len(page) // 2])
    return total

def main(input_path="input.txt"):
    rules, pages = parse_input(input_path)
    rule_map = get_rules(rules)
    result = sum_middle_of_valid_pages(rule_map, pages)
    print(result)

if __name__ == "__main__":
    main()