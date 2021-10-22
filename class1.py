import csv
import pandas as pd
import plotly.express as px


with open("C:/Users/Administrator/Desktop/Python/c105/class1.csv",newline = "")as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
totalmarks = 0
totalenties = len(filedata)

for marks in filedata:
    totalmarks += float(marks[1])

mean = totalmarks/totalenties
print("mean is "+ str(mean))

df = pd.read_csv("C:/Users/Administrator/Desktop/Python/c105/class1.csv")
fig = px.scatter(df,x="Student Number",y= "Marks")

fig.update_layout(shapes =[
    dict(type = "line",y0 = mean,y1 = mean,x0 = 0,x1 = totalenties)
])
#fig.update_yaxes(rangemode = "tozero")
fig.show()