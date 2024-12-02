import csv
from collections import Counter

# Datei öffnen und lesen
with open('./output.csv', mode='r') as file:
    reader = csv.reader(file)
    column_1 = []
    column_2 = []
    total_sum = 0
    total_similarity_score = 0

    for row in reader:
        column_1.append(int(row[0]))
        column_2.append(int(row[1]))

    column_1.sort()
    column_2.sort()

    for i in range(len(column_1)):
        total_sum += abs(column_1[i] - column_2[i])
    print(total_sum)
        
#Part two:
    counter = Counter(column_2)
    for i in range(len(column_1)):
        total_similarity_score += column_1[i] * counter[column_1[i]]
    print(total_similarity_score)
