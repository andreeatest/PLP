
import csv

reader_test = csv.reader(open('pass.csv'), delimiter=':', quotechar='|')
result = {}
for row in reader_test:
    result[row[0]] = row[2]
print(result)

download_dir = "output.csv"  # where you want the file to be downloaded to

csv = open(download_dir, "w")
# "w" indicates that you're writing strings to the file
columnTitleRow = "username, id\n"
csv.write(columnTitleRow)

for key in result.keys():
        name = key
        value = result[key]
        row = name + " " + value +"\n"
        csv.write(row)