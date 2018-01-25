import csv

reader_1 = csv.reader(open('pass.csv'), delimiter=':', quotechar='|')
result = {}
for row in reader_1:
    result[row[0]] = row[2]
print(result)

csv = open("output.csv", "w")

columnTitleRow = "username, id\n"
csv.write(columnTitleRow)

for key in result.keys():
        name = key
        value = result[key]
        row = name + " " + value +"\n"
        csv.write(row)