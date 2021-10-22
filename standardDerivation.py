import csv
import pandas
import math

with open("C:/Users/Administrator/Desktop/Python/c105/data.csv",newline = "")as f:
    reader = csv.reader(f)
    filedata = list(reader)

data = filedata.pop(0)
def mean(data):
    n = len(data)
    total = 0

    for x in data:
        total += int(x)
    mean = total/n
    return mean

#squarring
squaredlist = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squaredlist.append(a)

#getting sum
sum = 0
for i in squaredlist:
    sum = sum + i
    
#divide
result = sum/(len(data)-1)

#standard derivation
standardDerivation = math.sqrt(result)


print("the standard derivation is: ", standardDerivation)