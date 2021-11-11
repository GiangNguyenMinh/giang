import pygame as py
import random
from queue import PriorityQueue

WIDTH = 800
WIN = py.display.set_mode((WIDTH, WIDTH))
py.display.set_caption("A* Path finding Algorithm")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 255)
class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    def get_pos(self):
        return self.row, self.col
    def is_closed(self):
        return self.color == RED
    def is_open(self):
        return self.color == GREEN
    def is_barrier(self):
        return self.color == BLACK
    def is_star(self):
        return self.color == ORANGE
    def is_end(self):
        return self.color == TURQUOISE
    def reset(self):
        self.color = WHITE
    def make_start(self):
        self. color = ORANGE
    def make_closed(self):
        self.color = RED
    def make_open(self):
        self.color = GREEN
    def make_barrier(self):
        self.color = BLACK
    def make_end(self):
        self.color = TURQUOISE
    def make_path(self):
        self.col = PURPLE
    def draw(self, win):
        py.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # down
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # up
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # right
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # left
            self.neighbors.append(grid[self.row][self.col - 1])
        # cross
        # if self.col > 0 and self.row > 0 and not grid[self.row - 1][self.col - 1].is_barrier(): #upper lelf
        #     self.neighbors.append(grid[self.row - 1][self.col - 1])
        # if self.col > 0 and self.row < self.total_rows - 1 and not grid[self.row + 1][self.col - 1].is_barrier(): #lower lelf
        #     self.neighbors.append(grid[self.row + 1][self.col - 1])
        # if self.row > 0 and self.col < self.total_rows - 1 and not grid[self.row -1][self.col + 1].is_barrier(): # upper right
        #     self.neighbors.append(grid[self.row -1][self.col + 1])
        # if self.row < self.total_rows - 1 and self.col < self.total_rows - 1 and not grid[self.row + 1][self.col + 1].is_barrier(): # lower right
        #     self.neighbors.append(grid[self.row + 1][self.col + 1])
    def __lt__(self, other):
        return False
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)
def algorithm(draw, grid, start, end):
    cout = 0
    open_set = PriorityQueue()
    open_set.put((0, cout, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start}
    while not open_set.empty():
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            return True
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                pass

def make_grid(rows, width):
    gird = []
    gap = width // rows
    for i in range(rows):
        gird.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            gird[i].append(spot)
    return gird
def draw_gird(win, rows, width):
    gap = width // rows
    for i in range(rows):
        py.draw.line(win, GREY, (0, i*gap), (width, i * gap))
    for j in range(rows):
            py.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_gird(win, rows, width)
    py.display.update()
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col
def main(win, width,):
    ROWS = 50
    size = random.randint(ROWS*ROWS/2 - 100, ROWS*ROWS/2)
    random_map = []
    for i in range(size):
        y = random.randint(0, 49)
        x = random.randint(0, 49)
        random_map.append([y, x])
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if started:
                continue
            if py.mouse.get_pressed()[0]:
                pos = py.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            elif py.mouse.get_pressed()[2]:
                pos = py.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
            if event.type == py.KEYDOWN:
                if event.key == py.K_d:
                    start_y, start_x = random_map[0]
                    end_y, end_x = random_map[1]
                    start = grid[start_y][start_x]
                    start.make_start()
                    for i in range(random_map.count([start_y, start_x])):
                        random_map.remove([start_y, start_x])
                    end = grid[end_y][end_x]
                    end.make_end()
                    for i in range(random_map.count([end_y, end_x])):
                        random_map.remove([end_y, end_x])
                    if [end_y, end_x] in random_map:
                        random_map.remove([end_y, end_x])
                    for t in random_map:
                        barrier = grid[t[0]][t[1]]
                        barrier.make_barrier()
                if event.key == py.K_SPACE and not started:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                if event.key == py.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    py.quit()
main(WIN, WIDTH)




