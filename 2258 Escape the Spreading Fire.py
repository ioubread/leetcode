import sys


grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
hehexd = [[None, None, None, None], [None, None, None, None], [None, None, None, None]]



def getSpecsOfEntry(inputList):
    numberOfRows = len(inputList)
    numberOfColumns = len(inputList[0])

    return {"numberOfRows": numberOfRows, "numberOfColumns": numberOfColumns}


def generateEmptyList(specsToMoldItAfter):
    numberOfRows = specsToMoldItAfter["numberOfRows"]
    numberOfColumn = specsToMoldItAfter["numberOfColumns"]

    sampleGrid = []
    sampleRow = []
    for _ in range(numberOfColumn):
        sampleRow.append(None)

    for _ in range(numberOfRows):
        sampleGrid.append(sampleRow)


    return sampleGrid




def loopingThroughTheGrid(userSuppliedGrid):

    
    listOfValuableInformation = []

    specsOfThisGrid = getSpecsOfEntry(userSuppliedGrid)

    intRows = specsOfThisGrid["numberOfRows"]

    intColumns = specsOfThisGrid["numberOfColumns"]

    for i in range(len(userSuppliedGrid)):
        for j in range(len(userSuppliedGrid[0])):
            coordinateOfThisSpace = [i, j]
            
            valueSelf = userSuppliedGrid[i][j]


            try:
                valueLeft = grid[i][j-1]
            except:
                valueLeft =  None
            try:
                valueTop = grid[i-1][j]
            except:
                valueTop = None
            try:
                valueRight = grid[i][j+1]
            except:
                valueRight = None
            try:
                valueDown = grid[i+1][j]
            except:
                valueDown = None
            
            if i == 0:
                valueTop = None
            
            if j == 0:
                valueLeft = None



            theCoordinatesTho = [i, j]
            valuableInformation = {"coordinates": theCoordinatesTho, "self": valueSelf, "neighbours": [valueTop, valueDown, valueLeft, valueRight]}
            
            listOfValuableInformation.append(valuableInformation)
            


    return listOfValuableInformation



def changeValue(inputGrid, coordinates, targetValue):
    for i in range(len(inputGrid)):
        for j in range(len(inputGrid[0])):
            if [i, j] == coordinates:
                inputGrid[i][j] = targetValue
    
    return inputGrid


def setPersonAndGoal(inputGrid):
    width = len(inputGrid[0]) - 1
    height = len(inputGrid) - 1
    outputGrid = changeValue(inputGrid, [0,0], 3)
    outputGrid = changeValue(outputGrid, [height, width], 4)

    return outputGrid

def runItOnce(userinputValuableData, userinputEmptylist):

    returnGrid = userinputEmptylist.copy()

    for lineOfData in userinputValuableData:

        dataSelf = lineOfData["self"]
        coordinates = lineOfData["coordinates"]
        neighbours = lineOfData["neighbours"]

        prevValue = returnGrid[coordinates[0]][coordinates[1]]

        if dataSelf == 2:
            
            returnGrid[coordinates[0]][coordinates[1]] = 2
            returnGrid = changeValue(returnGrid, coordinates, 2)
        
        elif dataSelf == 0:
            if 1 in neighbours:
                returnGrid[coordinates[0]][coordinates[1]] = 1

            else:
                returnGrid[coordinates[0]][coordinates[1]] = 0

        elif dataSelf == 1:
            returnGrid[coordinates[0]][coordinates[1]] = 1

    return returnGrid




def main(userInputGrid):

    userInputGrid = setPersonAndGoal(userInputGrid)

    print(f"INITIAL")
    for line in userInputGrid:
        print(line)
    
    input()

    while True:

        specsOfUserInput = getSpecsOfEntry(userInputGrid)

        emptyList = generateEmptyList(specsOfUserInput)

        resultsFromLoopingTheList = loopingThroughTheGrid(userInputGrid)

    
        userInputGrid = runItOnce(resultsFromLoopingTheList, userInputGrid)

        for line in userInputGrid:
            print(line)
        
        input()


main(grid)