import math
import csv

with open('data.csv',newline='') as l:
    read= csv.reader(l)
    list= list(read)

data= list.pop(0)

def findingMean(file):
    lenght=len(file)

    totalMarks=0

    for marks in file:
        totalMarks+= int(marks)

    mean= totalMarks/lenght

    return mean
squareinformation=[]
for deviation in data:
    subtract= int(deviation)-findingMean(data)       
    squareData=subtract**2
    squareinformation.append(squareData)

sum=0

for i in squareinformation:
    sum=sum+i

answer=sum/(len(data)-1)

standardDeviation=math.sqrt(answer)

print('StandardDeviation is '+ str(standardDeviation))