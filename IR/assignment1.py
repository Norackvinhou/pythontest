import math
from unittest import result
import numpy  as np

data =  [
    [157,73,0,0,0,0],
    [4,157,0,1,0,0],
    [232,227,0,2,1,1],
    [0,10,0,0,0,0],
    [57,0,0,0,0,0],
    [2,0,3,5,5,1],
    [2,0,1,1,1,0]
]
#Calculate TF
for i in range (len(data)):
    for j in range (len(data[i])):
        if(data[i][j]==0):
            continue
        data[i][j]= math.log2(data[i][j])+1

#Calculate IDF
Antony = math.log2(3)
Brutus = math.log2(2)
Caesar = math.log2(6/5)
Calpurnia = math.log2(6)
Cleopatra = math.log2(6)
mercy = math.log2(6/5)
worser = math.log2(6/4)

re=[[],[],[],[],[],[],[]]
##TF-IDF
for i in range(7):
    if(i==0):
        for j in range(len(data[i])):
            
            re[i].append(round(data[i][j]*Antony,2))

for i in range(7):
    if(i==1):
        for j in range(len(data[i])):
            
            re[i].append(round(data[i][j]*Brutus,2))


for i in range(7):
    if(i==2):
        for j in range(len(data[i])):
            
            re[i].append(round(data[i][j]*Caesar,2))


for i in range(7):
    if(i==3):
        for j in range(len(data[i])):
            
            re[i].append(round(data[i][j]*Calpurnia,2))


for i in range(7):
    if(i==4):
        for j in range(len(data[i])):
            
            re[i].append(round(data[i][j]*Cleopatra,2))


for i in range(7):
    if(i==5):
        for j in range(len(data[i])):
            
            re[i].append(round(data[i][j]*mercy,2))


for i in range(7):
    if(i==6):
        for j in range(len(data[i])):
            
            re[i].append(round(data[i][j]*worser,2))

#print
# for i in re:
#     print(i)

#term-cor
arr = np.array(re)
tarr=np.transpose(arr)
result = np.matmul(arr,tarr)
print(result)