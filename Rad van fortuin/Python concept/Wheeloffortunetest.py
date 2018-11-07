import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

Averages = []
pricelist = []
List = []

# Aantal keren dat men een biertje haalt om een gemiddelde te berekenen
for x in range(1000):
    List.append(round(random.random()*360))

# Er zijn 24 taartpunten op de schijf hieronder zijn de prijzen verdeeld over
# deze punten per 2 of 4. Aangezien de schijf een stophoek kiest vanuit een
# uniforme verdeling zal er volgens onderstaande verhouding een gemiddelde prijs
# uitkomen. Hier gaan we er van uit dat deze 2,50 of hoger moet zijn.
for Value in List:
    if Value >= 0 and Value < 30: # 2
        pricelist.append(2.00)
    if Value >= 30 and Value < 60: # 2
        pricelist.append(2.20)
    if Value >= 60 and Value < 90: # 2
        pricelist.append(2.30)
    if Value >= 90 and Value < 150: # 4
        pricelist.append(2.40)
    if Value >= 150 and Value < 210: # 4
        pricelist.append(2.50)
    if Value >= 210 and Value < 240: # 2
        pricelist.append(2.60)
    if Value >= 240 and Value < 270: # 2
        pricelist.append(2.70)
    if Value >= 270 and Value < 30: # 2
        pricelist.append(2.80)
    if Value >= 300 and Value < 360: # 4
        pricelist.append(3.00)

average = sum(pricelist)/len(pricelist)
print("%.2f" % average)
labels, values = zip(*sorted(Counter(pricelist).items()))
indexes = np.arange(len(labels))
width = 1

# plt.bar(indexes, values, width)
# plt.xticks(indexes + width * 0.5, labels)
# plt.show()
