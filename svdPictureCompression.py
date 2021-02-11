import matplotlib.pyplot as plt
import numpy as num
import copy

def matrixFixer(matrix):
    temp=[]
    for j in range(len(matrix[0])):
        temp1=[]
        for i in range(len(matrix)):
         temp1.append(matrix[i][j])
        temp.append(temp1)
    return temp

img = plt.imread('2.ppm')
plt.imshow(img)
plt.show()
data = num.asarray(img)
#print(type(data))
#print(data.shape)
#print(data)
m = len(data)
n = len(data[0])
rgb=[]
rgbSvd=[]
temp=[]
Kvalues=[50,100,150]
#print(len(data))
#print(len(data[0]))
#print(len(data[0][0]))
"""for i in range(len(data)):
    temp=[]
    for j in range(len(data[0])):
        for k in range(len(data[0][0])):"""
for l in range(len(Kvalues)):
 img = plt.imread('2.ppm')

 data = num.asarray(img)
 # print(type(data))
 # print(data.shape)
 # print(data)
 m = len(data)
 n = len(data[0])
 rgb = []
 rgbSvd = []
 temp = []
 K=Kvalues[l]
 for i in range(len(data[0][0])):
     temp2=[]
     for j in range(len(data)):
         temp=[]
         for k in range(len(data[0])):
             temp.append(data[j][k][i])
         temp2.append(temp)
     rgb.append(temp2)
 rgb=num.asarray(rgb)
 #print("the data of rgb is")
 #print(rgb.shape)
 rgbTemp=[]
 for i in range(len(rgb)):
  rgbTemp.append(num.linalg.svd(rgb[i]))
  #print("the length of temp is  ")
  #print(len(temp))
  #print("the value of temp[0][0] is")
  #print(temp[0][0][0])
  #print(len(temp[0]))
  #print(len(temp[0][0]))
  #print("the value of temp[1] is")
  #print(temp[1][0])
  #print(len(temp[1]))
  #print("the value of temp[2] is")
  #print(temp[2][0][0])
  #print(len(temp[2]))
  #print(len(temp[2][0]))

 #print
 for i in range(len(rgbTemp)):
  rgbSvdTemp=[]
  for j in range(len(rgbTemp[i])):
   rgbSvdTemp.append(num.asarray(rgbTemp[i][j]))
  rgbSvd.append(rgbSvdTemp)

 #print("the data of rgbsv is")
 #print(rgbSvd.shape)
 #m=len(data)
 #n=len(data[0])
 #sigma1=[[0] for j in range(n)]
 #sigma=[sigma1 for i in range(m) ]
 #rgbSvd2=[[rgbSvd[0][0],sigma,rgbSvd[0][2]],[rgbSvd[1][0],sigma,rgbSvd[1][2]],[rgbSvd[2][0],sigma,rgbSvd[2][2]]]
 for i in range(len(rgbSvd)):
     diameter=rgbSvd[i][1]
     sigma1 = [0 for j in range(n)]
     sigma = [copy.deepcopy(sigma1) for i in range(m)]
     for j in range(len(diameter)):
         if(j<K):sigma[j][j]=float(diameter[j])
         else:sigma[j][j]=float(0)

     rgbSvd[i][1]=num.asarray(sigma)

 #print("the data is ")
 #print(rgbSvd[0][0].data)
 #print(rgbSvd[0][1].data)
 #print(rgbSvd[0][2].data)
 #print("and the type is")
 #print(type(rgbSvd[0][0]))
 #print(type(rgbSvd[0][1]))
 #print(type(rgbSvd[0][2]))
 #print("and the shape is")
 #print(rgbSvd[0][0].shape)
 #print(rgbSvd[0][1].shape)
 #print(rgbSvd[0][2].shape)

 multiplitedMatrixes=[]

 #rgbSvd[0][0].dot(rgbSvd[0][1])
 #print("the value of rgbvsd[0] is")

 for i in range(len(rgbSvd)):
  multiplitedMatrixes.append(rgbSvd[i][0].dot(rgbSvd[i][1].dot(rgbSvd[i][2])))
 #for i in range(len(multiplitedMatrixes)):
 # multiplitedMatrixes[i]=num.transpose(multiplitedMatrixes[i])
 #print("stop")
 #for i in range(len(multiplitedMatrixes)):
 # multiplitedMatrixes[i]=matrixFixer(multiplitedMatrixes[i])

 rgbRestord1 = [[] for j in range(n)]
 rgbRestord = [copy.deepcopy(rgbRestord1) for i in range(m)]

 for i in range(m):
  for j in range(n):
     for k in range(len(multiplitedMatrixes)):
         rgbRestord[i][j].append(int(multiplitedMatrixes[k][i][j]))

 rgbRestord=num.asarray(rgbRestord)
 #print(rgbSvd[0][0][0])

 plt.imshow(rgbRestord)
 plt.show()

 #print(len(rgbSvd))
 #print(len(rgbSvd[0][0]))
 #print("the value of rgbvsd[1] is")
 #print(rgbSvd[1][0])
 #print(len(rgbSvd[1]))
 #print(len(temp[0][0]))
 #print("the value of rgbvsd[2] is")
 #print(rgbSvd[2][0][0])
 #print(len(rgbSvd[2]))
 #print(len(rgbSvd[2][0]))



 #print("the length of rgb is")
 #print(print(len(rgb)))

 #plt.imshow(img)
 #plt.show()