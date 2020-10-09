import numpy as np 
from numpy.linalg import inv
print("enter the no of row")
n = int(input())

print("Enter the values row wise:")
matrix = []
while not matrix or len(matrix) < len(matrix[0]):
    matrix.append(list(map(float, input().split())))
#print(matrix)
#print(type(matrix))


numpymatrix= np.array(matrix)
numpymatrixP=np.around(numpymatrix,decimals=3)
total_0_axis = np.sum(numpymatrixP, axis=0)
total_1_axis = np.sum(numpymatrixP, axis=1)
print("The Given matrix  :")
print("----------------------")
print(numpymatrixP)
print("\n")
#print(numpymatrix.dtype)

print("----------------------")

#print(f'Sum of elements at column (0-axis) is {total_0_axis}')
#print(f'Sum of elements at Row (1-axis) is {total_1_axis}')

maxInRows = np.amax(total_1_axis)
maxInRowsP=np.around(maxInRows,decimals=3)
print("Max in the Sum of rows",maxInRowsP)
print("\n\n")

print("****************************** Compute  Casue and Effect using The DEMATEL Aprroach *******************************************")



print("\n\n")
print("The D matrix  :")
print("----------------------")
Dmatrix = numpymatrixP/  maxInRowsP
DM=np.around(Dmatrix,decimals=3)
print(DM)
print("\n\n")


print("The I matrix :")
print("----------------------")
IMatrix = np.identity(n)
IM=np.around(IMatrix,decimals=3)
print(IM)
print("\n\n")



print("The I-D matrix  :")
print("----------------------")
IminDmatrix = IM  - DM
IMinD=np.around(IminDmatrix,decimals=3)
print(IMinD)
print("\n\n")




print("The (I-D)^1 matrix :")
print("----------------------")
InversofIminDmatrix = np.linalg.inv(IMinD)
InverofmD=np.around(InversofIminDmatrix,decimals=3)
print(InverofmD)
print("\n\n")


print("The D*(I-D)^1 matrix  :")
print("----------------------")
TMatrix = np.matmul(DM  , InverofmD)
TM=np.around(TMatrix,decimals=3)
print(TM)
print("\n\n")


print("The Ri   values are   :")
print("----------------------")
Ri = np.sum(TM  ,axis= 1)
RiP=np.around(Ri,decimals=3)
print(RiP,"\t")



print("The Ci   values are   :")
print("----------------------")
Ci = np.sum(TM  ,axis= 0)
CiP=np.around(Ci,decimals=3)
print(CiP)
print("\n\n")






print("************************************************************************************************************************************")

print("The Ri+Ci   values are   :")
print("----------------------")
RiplusCi = RiP + CiP 
RiplusCiP=np.around(RiplusCi,decimals=3)
print(RiplusCiP)
print("\n\n")


print("The Ri-Ci   values are   :")
print("----------------------")
RiMinusCi = RiP - CiP 
RiMinusCiP=np.around(RiMinusCi,decimals=3)
print(RiMinusCiP)

print("************************************************************************************************************************************")


print("\n\n")

