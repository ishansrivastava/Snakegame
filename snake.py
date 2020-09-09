MAP_X = 20
MAP_Y = 20

class Direction:
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'

class Node:
    def __init__(self):
        self.x = -1
        self.y = -1
        self.next_node = None
        self.prev_node = None

class Snake:
    def __init__(self):
        self.head = None
        self.tail = None
        self.direction = None

    def initialize(self, x, y, initial_direction):
        self.head = self._get_new_node(x, y, None, None)
        self.tail = self.head
        self.direction = initial_direction

    def make_move(self, increase_length=False):
        new_x = -1
        new_y = -1
        if self.direction == Direction.LEFT:
            new_x = self.head.x - 1
            new_y = self.head.y
        elif self.direction == Direction.RIGHT:
            new_x = self.head.x + 1
            new_y = self.head.y
        elif self.direction == Direction.UP:
            new_x = self.head.x
            new_y = self.head.y - 1
        elif self.direction == Direction.DOWN:
            new_x = self.head.x
            new_y = self.head.y + 1
        else:
            assert False
        if new_x < 0:
            new_x = MAP_X - 1
        if new_x > MAP_X - 1:
            new_x = 0
        if new_y < 0:
            new_y = MAP_Y - 1
        if new_y > MAP_Y - 1:
            new_y = 0
        node = self._get_new_node(new_x, new_y, None, self.head)
        self.head.prev_node = node
        self.head = node
        if not increase_length:
            self.tail.prev_node.next_node = None
            self.tail = self.tail.prev_node

    def is_head_safe(self):
        temp = self.head.next_node
        while temp is not None:
            if temp.x == self.head.x and temp.y == self.head.y:
                return False
            temp = temp.next_node
        return True
        
    def _get_new_node(self, x, y, prev_node, next_node):
        node = Node()
        node.x = x
        node.y = y
        node.prev_node = prev_node
        node.next_node = next_node
        return node
