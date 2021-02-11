import pandas as pd

import numpy

import math

import matplotlib

import matplotlib.pyplot as pyplot

import copy

df =  pd.read_csv("total_cases.csv")
#print(df)
worldColumn = df["World"].tolist()
#worldColumn=worldColumn[0:(len(worldColumn)-7)]
#print(worldColumn)
results=[]
answer=[]
print("least square multipication values (b0 b1 b2) not considering the last seven days are")
for i in range(1,len(worldColumn)-6):
    results.append([1,i,math.pow(i,2)])

worldColumn=worldColumn[0:(len(worldColumn)-7)]
#a=numpy.array([[ 1,  1,0],
#     [ 1,  1,0],
#      [ 1,0 , 1],
#       [ 1,0,1]])
#b=numpy.array([1,3,8,2])
#answer=numpy.linalg.lstsq(a,b,rcond=-1)
#print("the answer1 is")
#print(answer)

a=numpy.array(results)

b=numpy.array(worldColumn)
answer=numpy.linalg.lstsq(a,b,rcond=-1)
answer=answer[0]
print(answer)
answerBasedOnSquareValues=[]
answerBasedOnrealvalues=[]
df =  pd.read_csv("total_cases.csv")
worldColumn= df["World"].tolist()
print("and the estimations for victoms of cronoa of the last seven days based on the least square values printed above are")
for i in range(len(worldColumn)-6,len(worldColumn)+1):
    #results.append([1,i,math.pow(i,2)])
    answerBasedOnSquareValues.append((answer[0])+(answer[1]*i)+(answer[2]*(math.pow(i,2))))
    print((answer[0])+(answer[1]*i)+(answer[2]*(math.pow(i,2))))
print("and real values for victoms of cronoa of the last seven days based on csv file are")
for i in range(len(worldColumn)-7,len(worldColumn)):
    #results.append([1,i,math.pow(i,2)])
    answerBasedOnrealvalues.append(worldColumn[i])
    print(worldColumn[i])
print("and the diffrence between estimated values and real values for cronoa victoms in order that they were introduced are")
average=0
for i in range(7):
    temp=answerBasedOnSquareValues[i]-answerBasedOnrealvalues[i]
    average=average+temp
    print(temp)
print("and average of the diffrence between estimated values and real values for cronoa victoms is")
print(average/7)


estimatedResults=[]

df =  pd.read_csv("total_cases.csv")

worldColumn = df["World"].tolist()

results=[]
answer=[]

for i in range(1,len(worldColumn)+1):
    results.append([1,i,math.pow(i,2)])


a=numpy.array(results)

b=numpy.array(worldColumn)
answer=numpy.linalg.lstsq(a,b,rcond=-1)
answer=answer[0]
print("x")
print(answer)
#print("the answer after complesion is")
#print(answer)

for i in range(len(worldColumn)):
    temp=answer[0]+answer[1]*i+answer[2]*math.pow(i,2)
    estimatedResults.append(temp)
#print(estimatedResults)
x=numpy.arange(1,len(worldColumn)+1,1)
x2=numpy.arange(1,len(worldColumn)+1,1)
#print(len(x))
#print(len(worldColumn))
#print(len(estimatedResults))
pyplot.plot(x2,estimatedResults)
pyplot.plot(x,worldColumn,'ro',markersize=2)
pyplot.show()

'''x=numpy.arange(1,6,1)
y=numpy.arange(7,12,1)
y2=numpy.arange(13,18,1)

pyplot.plot(x,y)
pyplot.plot(x,y2)
pyplot.show()
'''


pyplot.show()
#print(answer[0])
#print(answer)


