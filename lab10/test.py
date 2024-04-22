import csv

with open("data.csv", 'r', encoding="utf8") as csvfile:
    csvFile = csv.reader(csvfile)
    for lines in csvFile:
        print(lines)