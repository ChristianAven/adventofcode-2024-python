'''
URL chalenge: https://adventofcode.com/2024/day/2
answer: 356
'''

def is_sure_line(nums, max_diff):
    if len(nums) == 1:
        return True

    diffs = [b - a for a, b in zip(nums, nums[1:])]

    if any(d == 0 or abs(d) > max_diff for d in diffs):
        return False

    first_sign_pos = diffs[0] > 0
    return all((d > 0) == first_sign_pos for d in diffs)


def main(path='./input.txt', max_difference=3):
    sure_data = 0
    with open(path) as f:
        for line in f:
            tokens = line.split()
            if not tokens:
                continue
            nums = list(map(int, tokens))
            if is_sure_line(nums, max_difference):
                sure_data += 1
    print(sure_data)


if __name__ == "__main__":
    main()
