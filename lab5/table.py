import re
import csv

f = open("row.txt", "r", encoding="utf8")
text = f.read()

pattern = r"\n(?P<number>[0-9]+)\.\n(?P<name>.+)\n(?P<count>.+)x(?P<cost>.+)\n(?P<price>.+)\n"

matches = re.finditer(pattern, text)

with open("data.csv", 'w', newline='', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['number', 'name', 'count', 'price'])
    for x in matches:
            number = x.group('number').strip().replace('"', '')
            name = x.group('name').strip().replace('"', '')
            count = x.group('count').strip().replace('"', '')
            cost = x.group('cost').strip().replace('"', '')
            price = x.group('price').strip().replace('"', '')
            writer.writerow([number, name, count, price])