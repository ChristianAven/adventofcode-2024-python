'''
URL: https://adventofcode.com/2024/day/1#part2
answer: 26859182
'''
from collections import Counter
from inputs import listOfPlaces1, listOfPlaces2

counts = Counter(listOfPlaces2)

score = sum(place * counts[place] for place in listOfPlaces1)

print(score)