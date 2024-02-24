import re
import csv

# Define a custom dialect to handle the specific format of your CSV file
class MyDialect(csv.Dialect):
    delimiter = ','
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
    lineterminator = '\n'

csv.register_dialect('my_dialect', MyDialect)

f = open("row.txt", "r", encoding="utf8")
text = f.read()

pattern = r"\n(?P<number>[0-9]+)\.\n(?P<name>.+)\n(?P<count>.+)x(?P<cost>.+)\n(?P<price>.+)\n"

matches = re.finditer(pattern, text)

with open("data.csv", 'w', newline='', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, dialect='my_dialect')
    writer.writerow(['number', 'name', 'count', 'price'])
    for x in matches:
        writer.writerow([
            x.group('number').strip().replace('"', ''), 
            x.group('name').strip().replace('"', ''), 
            x.group('count').strip().replace('"', ''), 
            x.group('cost').strip().replace('"', ''), 
            x.group('price').strip().replace('"', '')])
