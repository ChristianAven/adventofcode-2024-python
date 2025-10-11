'''
URL: https://adventofcode.com/2024/day/5#part2
answer = 5353
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

def fix_page(page, rule_map):
    page = list(page)
    pos = {v: i for i, v in enumerate(page)}
    changed = True

    while changed:
        changed = False
        for a, successors in rule_map.items():
            pa = pos.get(a)
            if pa is None:
                continue
            for b in successors:
                pb = pos.get(b)
                if pb is not None and pb < pa:
                    item = page.pop(pb)
                    if pb < pa:
                        pa -= 1
                    insert_at = pa + 1
                    page.insert(insert_at, item)

                    if pb < insert_at:
                        for i in range(pb, insert_at):
                            pos[page[i]] = i
                        pos[item] = insert_at
                    else:
                        for i in range(insert_at, pb + 1):
                            pos[page[i]] = i
                        pos[item] = insert_at

                    changed = True
                    break
            if changed:
                break

    return page

def sum_middle_of_invalid_pages(rule_map, pages):
    total = 0
    for page in pages:
        if not page_is_valid(page, rule_map):
            fixed_page = fix_page(page, rule_map)
            total += int(fixed_page[len(fixed_page) // 2])
    return total

def main(input_path="input.txt"):
    rules, pages = parse_input(input_path)
    rule_map = get_rules(rules)
    result = sum_middle_of_invalid_pages(rule_map, pages)
    print(result)

if __name__ == "__main__":
    main()