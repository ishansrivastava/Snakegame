import time
import random
import threading

import sys, termios, tty, os

from snake import Snake, Direction, MAP_X, MAP_Y

WAIT_FOR_TIME = 1

SEED = 5
DIRECTION = []

random.seed(SEED)

def print_board(snake, food_x, food_y):
    board = [['.' for j in range(MAP_X)] for i in range(MAP_Y)]
    board[food_y][food_x] = '&'
    board[snake.head.y][snake.head.x] = '@'
    temp = snake.head.next_node
    while temp is not None:
        board[temp.y][temp.x] = '#'
        temp = temp.next_node
    for i in range(MAP_Y):
        print('\b' * MAP_Y + ''.join(board[i]))
    print()

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_input():
    global DIRECTION
    while True:
        key = getch()
        if key == 'p':
            break
        if key == Direction.LEFT and len(DIRECTION) > 0 and DIRECTION[-1] == Direction.RIGHT:
            continue
        if key == Direction.RIGHT and len(DIRECTION) > 0 and DIRECTION[-1] == Direction.LEFT:
            continue
        if key == Direction.UP and len(DIRECTION) > 0 and DIRECTION[-1] == Direction.DOWN:
            continue
        if key == Direction.DOWN and len(DIRECTION) > 0 and DIRECTION[-1] == Direction.UP:
            continue
        if key in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
            DIRECTION.append(key)
    os._exit(1)

def play():
    global DIRECTION, LAST_DIRECTION
    snake = Snake()
    snake.initialize(10, 10, Direction.RIGHT)
    food_x = int(random.random() * MAP_X)
    food_y = int(random.random() * MAP_Y)

    inp_thread = threading.Thread(target=get_input)
    inp_thread.start()
    while True:
        if len(DIRECTION) > 0:
            snake.direction = DIRECTION[0]
            DIRECTION = DIRECTION[1:]
        if snake.head.x == food_x and snake.head.y == food_y:
            snake.make_move(True)
            food_x = int(random.random() * MAP_X)
            food_y = int(random.random() * MAP_Y)
        else:
            snake.make_move()
        LAST_DIRECTION = DIRECTION
        print_board(snake, food_x, food_y)
        time.sleep(WAIT_FOR_TIME)

if __name__ == '__main__':
    play()
