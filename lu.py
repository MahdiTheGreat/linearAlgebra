import copy
#equationSystemSolver with mode 1 is forward-substitution and 2 is backward-substitution
#in mode 1 we use rowoperation1 and mode 2 we use rowoperation 2

def printMatrix(matrix):

    for i in range(len(matrix)):
     print("|",end=" ")
     for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
     print("|")
    print(" ")

def printAinverse(matrix):

    for i in range(len(matrix[0])):
     print("|",end=" ")
     for j in range(len(matrix)):
            print(matrix[j][i],end=" ")
     print("|")
    print(" ")


def pivotPosition(matrix, i, aug):
    j=-3
    for j in range(len(matrix[0])):
        if matrix[i][j]!=0:
            if j==n and aug==1:
                return -1
            else:
                #print("the  position of pivot found in pivotposition is"+str(j)+" "+str(i))
                return j
        elif j==n and aug==1:
            return -2
    return j


def rowMerger(matrix,pivotRow,i):
    for l in range(len(matrix[0])):
        matrix[i][l]=matrix[pivotRow][l]+matrix[i][l]
    printMatrix(matrix)


def rowOperation(matrix,pivotColumn,pivotRow,i):

    pivotElement=matrix[pivotRow][pivotColumn]
    temp=matrix[i][pivotColumn]/pivotElement

    #print("the pivot element and temp are in order:"+str(pivotElement)+" "+str(temp))

    """for k in range(len(matrix[0])):
        matrix[pivotRow][k]=matrix[pivotRow][k]*temp
        """

    """ print("matrix after temp multiply")
    printMatrix(matrix)"""

    for k in range(len(matrix[0])):
        matrix[i][k] = -matrix[pivotRow][k]*temp+matrix[i][k]

    #print("matrix after pivot temp  multiply")
    #printMatrix(matrix)

    #rowMerger(matrix,pivotRow,i)
    #print("matrix after row merge")

    #printMatrix(matrix)

def rowManager(matrix,L, pivotRow,aug):
    pivotColumn = pivotPosition(matrix, pivotRow,aug)
    pivotElement=0
    if pivotColumn!=-1 and pivotColumn!=-2 and pivotColumn!=-3:
        #print("pivot row "+str(pivotRow)+"pivot column"+str(pivotColumn))
        pivotElement=matrix[pivotRow][pivotColumn]
    #print("the pivot positon is" + str(pivotRow) + " " + str(pivotColumn))
    if L!=0 and pivotElement!=0:
        for r in range(pivotRow , len(matrix)):
            L[r][pivotColumn]=matrix[r][pivotColumn]/pivotElement

        #print("The L matrix in rowOperation is:")
        #printMatrix(L)
    #k=pivotRow+1
    for k in range(pivotRow+1, len(matrix)):
        if matrix[k][pivotColumn]!=0 and pivotColumn!=-1 and pivotColumn!=-2:
            rowOperation(matrix,pivotRow, pivotColumn, k)
        elif pivotColumn==-1 or pivotColumn==-2 or pivotColumn==-3:
            return pivotColumn
    return 0

def findAnswer(matrix,incons):

    #print("went inside findasnwer and incons is"+str(incons))

    if incons==-1:
        print("the system of equations is inconsistent")
        print("because we have a row of zeros in coefficients matrix(A)")
        print("but in that same row in b,we have a nonzero number which cant be possible ")
        print("if the system was consistent")
        return -1

    elif incons==-2:
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
            if (incons != -1 and incons != -2):
             #print("went to get pivotposition in findanswer")
             incons=pivotPosition(matrix, i,1)
             #print("the pivot or incons is"+str(incons))
             if (incons!=-1 and incons!=-2):
                 answer.append(matrix[i][len(matrix)] / matrix[i][incons])

        if (incons!=-1 and incons!=-2) :
         #print("the answer and matrix x is:")
         for i in range(0,len(answer)):
             """print("|", end=" ")
             print(answer[i], end=" ")
             print("|")
             """
         print(" ")
         return answer

        elif incons == -1:
            print("the system of equations is inconsistent")
            print("because we have a row of zeros in coefficients matrix(A)")
            print("but in that same row in b,we have a nonzero number which cant be possible ")
            print("if the system was consistent")
            return -1

        elif incons == -2:
            print("the system of equations has infinite answers ")
            print("because we have a row of zeros which shows that there are free variables")
            #print("which cant be possible if the system was consistent")
            return -2


def rowManager2(matrix,pivotRow,aug):
    pivotColumn = pivotPosition(matrix, pivotRow,aug)
    #print("the pivot positon is" + str(pivotRow) + " " + str(pivotColumn))
    k=pivotRow+1
    for k in range(pivotRow-1,-1,-1):
        if matrix[k][pivotColumn]!=0 and pivotColumn!=-1 and pivotColumn!=-2 :
            rowOperation(matrix, pivotRow, pivotColumn, k)
        elif pivotColumn==-1 or pivotColumn==-2:
            return pivotColumn
    return 0

# equationSystemSolver with mode 1 is forward-substitution and 2 is backward-substitution
   # in mode 1 we use rowoperation1 and mode 2 we use rowoperation 2

def equationSystemSolver(matrix,b,mode):



   incons=0

   for i in range(0,len(matrix)):
       matrix[i].append(b[i])

   for i in range(0,len(matrix)):
        if incons == 0 and (mode==1 or mode==0):
            incons = rowManager(matrix,0,i,1)

   for i in range(0,len(matrix)):
        if incons == 0 and (mode==2 or mode==0):
            incons = rowManager2(matrix,i,1)


   #print("last matrix")

   #printMatrix(matrix)

   # if incons==0:

   return findAnswer(matrix, incons)

#rowData=""
incons=0
n=int(input())

matrix=[[]for j in range(0,n)]
for i in range(0,n):
   matrix[i]=[[]for j in range(0,n)]

L=[[]for k in range(0,n)]
for i in range(0,n):
   L[i]=[[]for j in range(0,n)]

for i in range(0,n):
    for j in range(0,n):
        L[i][j]=0
for i in range(0, n):
    L[i][i] = 1

'''if L!=0:
 print("true")
 '''

identity=[[]for k in range(0,n)]
for i in range(0,n):
   identity[i]=[[]for j in range(0,n)]


for i in range(0,n):
    for j in range(0,n):
        identity[i][j]=0
for i in range(0, n):
    identity[i][i] = 1

#answer=[[]for k in range(0,n)]

for i in range(0,len(matrix)):
    rowData=input()
    matrix[i]=rowData.split()

for i in range(0,len(matrix)):
    matrix[i]=[float(matrix[i][j]) for j in range(0,len(matrix))]

print("the matrix is:")

printMatrix(matrix)

for i in range(0,len(matrix)):
    if incons==0:
     incons=rowManager(matrix,L,i,0)

answer=[]
print("L is:")
printMatrix(L)

print("U is:")
printMatrix(matrix)

for i in range(0,n):

   l=copy.deepcopy(L)
   u=copy.deepcopy(matrix)

   # equationSystemSolver with mode 1 is forward-substitution and 2 is backward-substitution
   # in mode 1 we use rowoperation1 and mode 2 we use rowoperation 2

   answer.append(equationSystemSolver(u,equationSystemSolver(l,identity[i],1),2))
   #print("answer is:")
   #print(answer)


print("the inverse of A is:")

printAinverse(answer)


