'''
URL chalenge: https://adventofcode.com/2024/day/2#part2
answer: 413
'''

def is_sure_line(nums, max_diff=3):
    
    length_of_nums = len(nums)
    if length_of_nums <= 2:
        return True
    
    index = 0
    
    while length_of_nums > index:
        new_nums = nums[:index] + nums[index+1:] # remove one element
        is_ascending = new_nums[1] > new_nums[0]
        
        diffs = [b - a for a, b in zip(new_nums, new_nums[1:])] # get differences
        is_ordered = all((b > 0) == is_ascending for b in diffs) # check if all differences have the same sign
        is_within_diff = all(0 < abs(b) <= max_diff for b in diffs) # check if all differences are within the max difference
        if is_ordered and is_within_diff:
            return True

        index += 1
    return False    

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