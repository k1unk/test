import random

SIZE = 20 
VALUE = 3

arr = [[0] * SIZE for i in range(SIZE)]
for i in range(SIZE):
    for j in range(SIZE):
        arr[i][j] = [random.randint(0, 1), False]

def isWater(i,j):
    if (arr[i][j][0] == 0):
        return True
    return False

def isCheckNeeded(i, j):
    if (isWater(i,j) or arr[i][j][1] == True):
        return False
    return True

def checkRight(i, j):
    if (j!=SIZE-1):
        if (arr[i][j+1][0] == 1 and (i*SIZE+j+1) in islandCells2 and islandCells2[i*SIZE+j+1]!=True
        or arr[i][j+1][0] == 1 and (i*SIZE+j+1) not in islandCells2):
            islandCells.append([i, j+1])
            islandCells2[i*SIZE+j+1] = False

def checkLeft(i, j):
    if (j!=0):
        if (arr[i][j-1][0] == 1 and (i*SIZE+j-1) in islandCells2 and islandCells2[i*SIZE+j-1]!=True
        or arr[i][j-1][0] == 1 and (i*SIZE+j-1) not in islandCells2 ):
            islandCells.append([i, j-1])
            islandCells2[i*SIZE+j-1] = False

def checkDown(i, j):
    if (i!=SIZE-1):
        if (arr[i+1][j][0] == 1 and ((i+1)*SIZE+j) in islandCells2 and islandCells2[(i+1)*SIZE+j]!=True
        or arr[i+1][j][0] == 1 and ((i+1)*SIZE+j) not in islandCells2):
            islandCells.append([i+1, j])
            islandCells2[(i+1)*SIZE+j] = False

def checkNearCells(i, j, count):
    islandCells2[i*SIZE+j] = True
    count = count + 1
    checkRight(i, j)
    checkLeft(i, j)
    checkDown(i, j)
    return count

def printArray():
    print()
    for i in range(SIZE):
        for j in range(SIZE):
            print(arr[i][j][0], "", end = '')
        print()

printArray()
for i in range(SIZE):
    for j in range(SIZE):
        if (isCheckNeeded(i, j)):
            islandCells = [[i, j]]
            islandCells2 = {i*SIZE+j: False}
            count=0
            while(len(islandCells)!=count):
                count = checkNearCells(islandCells[count][0], islandCells[count][1], count)
           
            if (len(islandCells)<VALUE):
                for k in islandCells2:
                    arr[k//SIZE][k%SIZE] = [0, False]
            else:
                for k in islandCells2:
                    arr[k//SIZE][k%SIZE] = [1, True]
            
printArray()
