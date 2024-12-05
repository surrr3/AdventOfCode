import re

directions_t1 = [(0,1),(1,0),(1,1),
              (0,-1),(-1,0),(-1,-1),
              (-1,1),(1,-1)]

directions_t2 = [(1,1),(-1,1)]

word = "XMAS"


def getData():

    searchGrid = []

    f = open("dayFourInput.txt", "r")

    for line in f:
        line = line.strip()
        searchGrid += [[char for char in line]]

    return searchGrid


def task1(searchGrid):

    counter = 0

    for i in range(len(searchGrid)):
        for j in range(len(searchGrid[i])):

            if searchGrid[i][j] == 'X':
                counter+=findMatch(i,j,searchGrid)

    return counter

def findMatch(i,j,searchGrid):

    counter = 0

    for direction in directions_t1:
        if searchDirection(direction,searchGrid,i,j):
            counter+=1
        
    return counter

def searchDirection(direction,searchGrid,i,j):

    x,y = direction

    try:
        for k in range(1,4):
            if i+(k*x) < 0 or j+(k*y) < 0:
                return False
            if searchGrid[i+(k*x)][j+(k*y)] != word[k]:
                return False
            
    except IndexError:

        return False
    
    return True

def task2(searchGrid):

    counter = 0

    for i in range(len(searchGrid)):
        for j in range(len(searchGrid[i])):

            if searchGrid[i][j] == 'A':
                counter+=findMas(i,j,searchGrid)

    return counter

def findMas(i,j,searchGrid):

    try:
        for pair in directions_t2:
            
            x,y = pair

            if ( searchGrid[i+x][j+y] == "M" and searchGrid[i-x][j-y] == "S" ) or \
            (searchGrid[i+x][j+y] == "S" and searchGrid[i-x][j-y] == "M" ):

                if i + x < 0 or j+y < 0 or i-x < 0 or j-y < 0:
                    return False    
                
                continue
            else:
                return False
            
    except IndexError:
        return False

    return True

if __name__ == "__main__":

    data = getData()

    print(f"Task 1: {task1(data)}")
    
    print(f"Task 2: {task2(data)}")




