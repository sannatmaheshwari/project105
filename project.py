import math
import csv

data = [60,61,65,63,98,99,90,95,91,96]
totalMarks = 0
totalEntries = len(data)
for marks in data:
    totalMarks+=float(marks)

mean = totalMarks/totalEntries

squaredList = []
for num in data:
    a = int(num)-mean
    a = a**2 
    squaredList.append(a)

sum = 0
for i in squaredList:
    sum = sum+i

result = sum/(totalEntries-1)
sd = math.sqrt(result)
print(sd)