from collections import Counter
from inputs import listOfPlaces1, listOfPlaces2

counts = Counter(listOfPlaces2)

score = sum(place * counts[place] for place in listOfPlaces1)

print(score)