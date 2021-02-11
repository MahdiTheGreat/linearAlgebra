import copy
import math
#equationSystemSolver with mode 1 is forward-substitution and 2 is backward-substitution
#in mode 1 we use rowoperation1 and mode 2 we use rowoperation 2

def makeASubMatrixByColumns(matrix,columns):
    subMatrix=[]
    subMatrix = [[] for j in range(0, len(matrix))]
    for i in range(0, len(matrix)):
        subMatrix[i] = [[] for j in range(0,len(columns))]
    for i in range(0, len(matrix)):
        subMatrix[i] = [matrix[i][columns[j]] for j in range(0, len(columns))]
    #print("the submatrix is ")
    #printMatrix(subMatrix)
    return subMatrix

def unAugment(matrix):
    length=len(matrix[0])-1
    for i in range(len(matrix)):
        matrix[i]=matrix[i][0:length]
    return matrix

def columnInarray(matrix,column):
    array=[]
    for i in range(len(matrix)):
        array.append(matrix[i][column])
    return array

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def truncateMatrix(matrix,precision):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j]=truncate(matrix[i][j],precision)
            matrix[i][j]=float(matrix[i][j])

def printMatrix(matrix):

    for i in range(len(matrix)):
     print("|",end=" ")
     for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
     print("|")
    print(" ")

def printUnaugmentMatrix(augmatrix):
    for i in range(len(matrix)):
     print("|",end=" ")
     for j in range(len(matrix[0])-1):
            print(matrix[i][j],end=" ")
     print("|")
    print(" ")

def findPivotColumns(matirx):
    pivotColList=[]
    for i in range(len(matrix)):
        flag=0
        pivotColumn=pivotPosition(matrix,i,1)
        if(pivotColumn!=-1 and pivotColumn!=-2 and pivotColumn!=-3 and flag==0):
            pivotColList.append(pivotColumn)
            flag=1

    return pivotColList

def findPivotPoints(matirx):

    pivotLocList=[]
    for i in range(len(matrix)):
        pivotColumn=pivotPosition(matrix,i,1)
        if(pivotColumn!=-1 and pivotColumn!=-2 and pivotColumn!=-3 ):
            pivotLocList.append([i,pivotColumn])

    return pivotLocList

def findRowBases(matrix):
    rowBases=[]
    for i in range(len(matrix)):
        flag=0
        for j in range(len(matrix[0])):
            if(flag!=1 and matrix[i][j]!=0):
                #print("the matrix element in find rowbases is "+str(matrix[i][j]))
                rowBases.append(i)
                flag=1
    return rowBases

def listCheck(list,key):

    for i in range(len(list)):
        if(key==list[i]):return i
    return -1


def printAnswer(matrix):

     """for j in range(len(matrix)):
         print("|",end=" ")
         print(truncate(matrix[j],6))
         print("|")"""
     for i in range(len(matrix)):
         print("|", end=" ")
         for j in range(1):
             print(truncate(matrix[i],6), end=" ")
         print("|")
     print(" ")





def pivotPosition(matrix, i, aug):
    j=-3
    for j in range(len(matrix[0])):
        if(matrix[i][j]!=0):
            if j==len(matrix) and aug==1:
                return -1
            else:
                #print(" in pivotposition method the  position of pivot found in pivotposition is "+str(i)+" "+str(j)+"and pivot element is "+str(matrix[i][j]))
                return j
        elif j==len(matrix) and aug==1:
            return -2
    return j


def rowMerger(matrix,pivotRow,i):
    for l in range(len(matrix[0])):
        matrix[i][l]=matrix[pivotRow][l]+matrix[i][l]
def pivotCheck(pivotpoints,j):
    for k in range(len(pivotpoints)):
        if( pivotpoints[k][1]==j):return True
    return False
def nullbase(matrix):

    pivotPoints = findPivotPoints(matrix)
    nullbase=[]

    for i in range(len(pivotPoints)):
        temp=matrix[pivotPoints[i][0]][pivotPoints[i][1]]
        temp2=[]
        #print("temp is " + str(temp))
        if(temp!=0):
            for j in range(len(matrix[0])-1):
                if (not pivotCheck(pivotPoints,j)):
                    temp2.append(-matrix[pivotPoints[i][0]][j]/temp)
            nullbase.append(temp2)


    num = len(matrix[0]) - len(pivotPoints)
    #temp = [0 for j in range(num)]
    nullbaseCompleteVersion=[]
    pivotNumber=0
    freeNumber=0
    for j in range(len(matrix[0])-1):
     check= pivotCheck(pivotPoints, j)
     if(check):
         nullbaseCompleteVersion.append(nullbase[pivotNumber])
         pivotNumber=pivotNumber+1
     else:
         temp = [0 for j in range(num)]
         temp[freeNumber]=1
         freeNumber=freeNumber+1
         nullbaseCompleteVersion.append(temp)




    #print("the nulbases are in array form")
    #print(nullbaseCompleteVersion)
    print("the nulbases are the columns printed in the matrix below ")
    truncateMatrix(nullbaseCompleteVersion,6)
    printMatrix(nullbaseCompleteVersion)




def rowOperation(matrix,pivotRow,pivotColumn,i):

    pivotElement=matrix[pivotRow][pivotColumn]
    #print("pivot element in rowoperation is "+str(pivotElement))
    if(matrix[i][pivotColumn]!=0 and pivotElement!=0):
     temp=matrix[i][pivotColumn]/pivotElement


     #print("temp  in rowoperation is: "+str(temp))

     for k in range(len(matrix[0])):
         matrix[i][k] =-matrix[pivotRow][k]*temp+matrix[i][k]

    #print("matrix after pivot temp  multiply")
    #printMatrix(matrix)


def rowManager(matrix ,pivotRow,aug):
    pivotColumn = pivotPosition(matrix, pivotRow,aug)

    for k in range(pivotRow+1, len(matrix)):
        if matrix[k][pivotColumn]!=0 and pivotColumn!=-1 and pivotColumn!=-2 and pivotColumn!=-3 :
            rowOperation(matrix,pivotRow, pivotColumn, k)
        elif pivotColumn==-1 or pivotColumn==-2 or pivotColumn==-3:
            return pivotColumn
    return 0

def findAnswer(matrix,incons,mode):

    #print("went inside findasnwer and incons is"+str(incons))

    if (incons==-1 and mode==0):
        print("the system of equations is inconsistent")
        print("because we have a row of zeros in coefficients matrix(A)")
        print("but in that same row in b,we have a nonzero number which cant be possible ")
        print("if the system was consistent")
        return -1

    elif(incons==-2 and mode==0):
        print("the system of equations has infinite answers  ")
        print("because we have a row of zeros which shows that there are free variables")
        #print("which cant be possible if the system was consistent")
        return -2

    else:

        #print("went inside last else")
        answer=[]
        incons=0

        for i in range(0,len(matrix)):
            #print("i is now"+str(i))
            if ((incons != -1 and incons != -2)or mode==1):
             #print("went to get pivotposition in findanswer")
             incons=pivotPosition(matrix, i,1)
             #print("the pivot or incons is"+str(incons))
             if ((incons!=-1 and incons!=-2) or mode==1):
                 if(matrix[i][incons]!=0):
                  answer.append(matrix[i][len(matrix[0])-1] / matrix[i][incons])


        if ((incons!=-1 and incons!=-2)or mode==1) :
         #print("the answer and matrix x is:")
         for i in range(0,len(answer)):
             """print("|", end=" ")
             print(answer[i], end=" ")
             print("|")
             """
         print(" ")
         return answer

        elif (incons==-2 and mode==0):
            print("the system of equations is inconsistent")
            print("because we have a row of zeros in coefficients matrix(A)")
            print("but in that same row in b,we have a nonzero number which cant be possible ")
            print("if the system was consistent")
            return -1

        elif (incons==-2 and mode==0) :
            print("the system of equations has infinite answers ")
            print("because we have a row of zeros which shows that there are free variables")
            #print("which cant be possible if the system was consistent")
            return -2


def rowManager2(matrix,pivotRow,aug):
    pivotColumn = pivotPosition(matrix, pivotRow,aug)
    #print("the pivot positon is" + str(pivotRow) + " " + str(pivotColumn))
    #k=pivotRow+1
    for k in range(pivotRow-1,-1,-1):
        if matrix[k][pivotColumn]!=0 and pivotColumn!=-1 and pivotColumn!=-2 :
            rowOperation(matrix, pivotRow, pivotColumn, k)
        elif pivotColumn==-1 or pivotColumn==-2:
            return pivotColumn
    return 0

# equationSystemSolver with mode 1 is forward-substitution and 2 is backward-substitution
   # in mode 1 we use rowoperation1 and mode 2 we use rowoperation 2

def equationSystemManager(matrix,b,mode,solve,colBase,rowBase,nullBase,echelon):

   incons=0
   subMatrix=[]
   pivotColList=[]
   nonPivotColList=[]

   if(mode==0):
    for i in range(0,len(matrix)):
        matrix[i].append(b[i])
   #if(solve):
       #print("stiched together matrix is")
       #printMatrix(matrix)

   untouchedMatrix = copy.deepcopy(matrix)
   #print("the untouchedmatrix is ")
   #printMatrix(untouchedMatrix)

   #print("the matrix in equastion system manager is ")
   #printMatrix(matrix)
   pivotColList=[]

   for i in range(0,len(matrix)):
        if  (mode==1 or mode==0):
            incons = rowManager(matrix,i,1)

   truncateMatrix(matrix, 6)
   #print("after turnication")

   for i in range(0,len(matrix)):
        if  (mode==2 or mode==0):
            incons = rowManager2(matrix,i,1)

   #print("after echoleon upperform in eqautionsystem solver ")
   #printMatrix(matrix)
   truncateMatrix(matrix, 6)
   #print("after turnication")
   if(echelon==1):
       print("the extended echelon matrix is")
       printMatrix(matrix)


   if (colBase):
    pivotColList = findPivotColumns(matrix)
    print("the indexes of base ( entry ) matrix columns which are bases of col(A) in order from left to right are  ")
    for i in range(len(pivotColList)):
        print(pivotColList[i] + 1)
        print(" ")

    for j in range(len(untouchedMatrix[0]) - 1):
       flag = 0

       for i in range(len(pivotColList)):
        if (j == pivotColList[i]): flag += 1

       if (flag == 0):
            nonPivotColList.append(j)


   if(rowBase):
    rowBaselist = findRowBases(matrix)
    print("the indexs of matrix rows in the printed matrix below ")
    printUnaugmentMatrix(matrix)
    print("which are bases of rowA are in order from left to right are")
    for i in range(len(rowBaselist)):
        print(rowBaselist[i] + 1)
        print(" ")

    #print("matrix before nullbase")
    #print(matrix)
    if(nullBase):
        #print("from now on pivot position is imporant")
        #print("matrix before augmentation is")
        #printMatrix(matrix)
        # matrix=unAugment(matrix)
        #print("matrix after augmentation is")
        #printMatrix(matrix)
        nullbase(matrix)

    if(colBase):
     answer = []
     subMatrix = makeASubMatrixByColumns(untouchedMatrix, pivotColList)
     #print("submatrix is")
     #printMatrix(subMatrix)
     print("the indexes of columns in base(entry) matrix which were not pivot and are not in the base of col(A) in order from left to right")
     for i in range(len(nonPivotColList)):
         print(nonPivotColList[i] + 1)
         print(" ")
     print("and the coordination of the columns that are not pivot and therefor not in the base of colA,based on columns in the base of col(A) in order from left to right are")
     for j in range(len(untouchedMatrix[0]) - 1):
         # print("the length of untouched matrix is "+str(len(untouchedMatrix[0])-1))
         subMatrix = makeASubMatrixByColumns(untouchedMatrix, pivotColList)

         flag = 0

         for i in range(len(pivotColList)):
             if (j == pivotColList[i]): flag += 1

         if (flag == 0):
             answer.append(equationSystemManager(subMatrix, columnInarray(untouchedMatrix, j), 0, 1, 0, 0,0,0))

     truncateMatrix(answer, 6)
     print(answer)
     print("also the the value of the coordinates are based on the columbs in the base of colA in order they were introduced ")

   #print("last matrix")

   #printMatrix(matrix)

   # if incons==0:

   if(solve):
       #print("stoppoint")
       return findAnswer(matrix,incons,mode)

#MAIN

#incons=0
matrixSpec= [[] for j in range(0, 2)]
temp=input()
matrixSpec=temp.split()
for i in range(0,2):
    matrixSpec[i]=int(matrixSpec[i])

#print("the specs are"+str(matrixSpec[0])+" "+str(matrixSpec[1]))

matrix=[[]for j in range(0,matrixSpec[0])]
b=[[]for j in range(0,matrixSpec[0])]
for i in range(0,len(b)):
   b[i]=0

for i in range(0,len(matrix)):
   matrix[i]=[[]for j in range(0,(matrixSpec[1]))]

#pivotColList = []

#print("the matrix is ")
#printMatrix(matrix)

for i in range(0,len(matrix)):
    rowData=input()
    matrix[i]=rowData.split()

#print("the legth of matrix colums is "+str(len(matrix[0])))

for i in range(0,len(matrix)):
    matrix[i]=[float(matrix[i][j]) for j in range(0,len(matrix[0]))]


#printMatrix(matrix)


equationSystemManager(matrix,b,0,0,1,1,1,1)




