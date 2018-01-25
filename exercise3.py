
import csv
# from collections import defaultdict
#
# columns = defaultdict(list) # each value in each column is appended to a list
#
# with open('pass.csv') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         for (i,v) in enumerate(row):
#
#             columns[i].append(v)
# print(columns[0])

import csv

reader_1 = csv.reader(open('pass.csv'), delimiter=':', quotechar='|')
result = {}
for row in reader_1:
    result[row[0]] = row[2]
print(result)

# with open('output.csv', 'w') as f:
    # o = csv.writer(f)
    # o.writerow(result)
    # print()

    # dic = {"John": "john@example.com", "Mary": "mary@example.com"}  # dictionary
    #
download_dir = "output.csv"  # where you want the file to be downloaded to
    #
csv = open(download_dir, "w")
# "w" indicates that you're writing strings to the file
columnTitleRow = "username, id\n"
csv.write(columnTitleRow)

for key in result.keys():
        name = key
        email = result[key]
        row = name + " " + email + "\n"
        csv.write(row)