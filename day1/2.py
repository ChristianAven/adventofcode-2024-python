from collections import Counter
from inputs import listOfPlaces1, listOfPlaces2

# Contamos cuántas veces aparece cada número en listOfPlaces2
counts = Counter(listOfPlaces2)

# Calculamos el score recorriendo listOfPlaces1 una sola vez
score = sum(place * counts[place] for place in listOfPlaces1)

print(score)