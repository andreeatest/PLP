import json

json_d = json.load(open("9a.json"))
json_d2 = json.load(open("9b.json"))
math = []
science = []
lit = []
for i in json_d:
    math.append(i['math'])
    science.append(i['science'])
    lit.append(i['literature'])
for i in json_d2:
    math.append(i['math'])
    science.append(i['science'])
    lit.append(i['literature'])

print(math)
print("science: ", "min: ",min(science), "max: ", max(science),  "average: ", sum(science)/len(science))
print("literature: ","min: ",min(lit), "max: ", max(lit), "average: ", sum(lit)/len(lit))
print("math:", "min: ",min(math), "max:", max(math), "average: ", sum(math)/len(math))
