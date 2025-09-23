'''
URL of challenge: https://adventofcode.com/2024/day/1
answer: 1320851
'''
from inputs import listOfPlaces1, listOfPlaces2

sorted_list1, sorted_list2 = sorted(listOfPlaces1), sorted(listOfPlaces2)
distance = sum(abs(a - b) for a, b in zip(sorted_list1, sorted_list2))
print(distance)