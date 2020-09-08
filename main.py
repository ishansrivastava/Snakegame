import math
import random
import sys
import time
import threading
from collections import deque


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


random.seed(42)
columns = 10
rows = 10
llist = deque()
snakeMatrix = [["." for x in range(columns)] for y in range(rows)]


def food(row, column):
    global foodRow
    global foodColumn
    foodRow = row
    foodColumn = column
    snakeMatrix[foodRow][foodColumn] = "*"


def createSnakeMatrix():
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    global snakeRow
    global snakeColumn
    snakeRow = 5
    snakeColumn = 5
    snakeMatrix[snakeRow][snakeColumn] = "+"
    food(random.randrange(0, 10), random.randrange(0, 10))


def displayMatrix():
    for i in range(0, 10):
        print(snakeMatrix[i])
    print("\n")


def distanceFromFood(row, column):
    if row < 0 or row > 9 or column < 0 or column > 9:
        return 1000
    else:
        return (math.sqrt((pow(row - foodRow, 2) + pow(column - foodColumn, 2))))

def timerCalc():
    while(true):
        displayMatrix()
        print("Enter Input:")
        global x = input()
        time.sleep(1)

def snakeMoves():
    currentRow = snakeRow
    currentColumn = snakeColumn
    llist.append(Coordinates(snakeRow, snakeColumn))
    list(llist)
    while True:
        if len(llist) == rows * columns:
            print("Congratulations you won!!")
            break;
        move = x
        if move == 'w':
            if (llist[-1].x - 1) < 0 or snakeMatrix[llist[-1].x - 1][llist[-1].y] == '+':
                print("Dead...")
                break
            elif llist[-1].x - 1 == foodRow and llist[-1].y == foodColumn:
                snakeMatrix[llist[-1].x - 1][llist[-1].y] = "+"
                displayMatrix()
                llist.append(Coordinates(llist[-1].x - 1, llist[-1].y))
                food(int(random.random() * 10), int(random.random() * 10))
                displayMatrix()
            else:
                snakeMatrix[llist[-1].x - 1][llist[-1].y] = "+"
                snakeMatrix[llist[0].x][llist[0].y] = "."
                displayMatrix()
                llist.append(Coordinates(llist[-1].x - 1, llist[-1].y))
                llist.popleft()
        elif move == 's':
            if (llist[-1].x + 1) > 9 or snakeMatrix[llist[-1].x + 1][llist[-1].y] == '+':
                print("Dead..")
                break
            elif llist[-1].x + 1 == foodRow and llist[-1].y == foodColumn:
                snakeMatrix[llist[-1].x + 1][llist[-1].y] = '+'
                displayMatrix()
                llist.append(Coordinates(llist[-1].x + 1, llist[-1].y))
                food(int(random.random() * 10), int(random.random() * 10))
                displayMatrix()
            else:
                snakeMatrix[llist[-1].x + 1][llist[-1].y] = '+'
                snakeMatrix[llist[0].x][llist[0].y] = '.'
                displayMatrix()
                llist.append(Coordinates(llist[-1].x + 1, llist[-1].y))
                llist.popleft()
        elif move == 'a':
            if (llist[-1].y - 1) < 0 or snakeMatrix[llist[-1].x][llist[-1].y - 1] == '+':
                print("Dead..")
                break
            elif llist[-1].x == foodRow and llist[-1].y - 1 == foodColumn:
                snakeMatrix[llist[-1].x][llist[-1].y - 1] = '+'
                displayMatrix()
                llist.append(Coordinates(llist[-1].x, llist[-1].y - 1))
                food(int(random.random() * 10), int(random.random() * 10))
                displayMatrix()
            else:
                snakeMatrix[llist[-1].x][llist[-1].y - 1] = '+'
                snakeMatrix[llist[0].x][llist[0].y] = '.'
                displayMatrix()
                llist.append(Coordinates(llist[-1].x, llist[-1].y - 1))
                llist.popleft()
        elif move == 'd':
            if llist[-1].y + 1 > 9 or snakeMatrix[llist[-1].x][llist[-1].y + 1] == '+':
                print("Dead..")
                break
            elif llist[-1].x == foodRow and llist[-1].y + 1 == foodColumn:
                snakeMatrix[llist[-1].x][llist[-1].y + 1] = '+'
                displayMatrix()
                llist.append(Coordinates(llist[-1].x, llist[-1].y + 1))
                food(int(random.random() * 10), int(random.random() * 10))
                displayMatrix()
            else:
                snakeMatrix[llist[-1].x][llist[-1].y + 1] = '+'
                snakeMatrix[llist[0].x][llist[0].y] = '.'
                displayMatrix()
                llist.append(Coordinates(llist[-1].x, llist[-1].y + 1))
                llist.popleft()
        else:
            print("Wrong Input Please press right button\n")
        print("snake length:", len(llist))

if __name__ == '__main__':
    createSnakeMatrix()
    thread.start_new_thread(timerCalc, ())
    thread.start_new_thread(snakeMoves,())



        # displayMatrix()
        # for i in range(0,len(llist)):
        # print("(",llist[i].x,",",llist[i].y,")",",")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/