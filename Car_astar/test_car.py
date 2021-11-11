import pygame
import math
from queue import PriorityQueue
import random
from tkinter import messagebox, Tk

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


clock = pygame.time.Clock()
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return [self.row, self.col]

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_space(self):
        return self.color == WHITE

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    # cross
    # 	if self.col > 0 and self.row > 0 and not grid[self.row - 1][self.col - 1].is_barrier(): #upper lelf
    # 		self.neighbors.append(grid[self.row - 1][self.col - 1])
    # 	if self.col > 0 and self.row < self.total_rows - 1 and not grid[self.row + 1][self.col - 1].is_barrier(): #lower lelf
    # 		self.neighbors.append(grid[self.row + 1][self.col - 1])
    # 	if self.row > 0 and self.col < self.total_rows - 1 and not grid[self.row -1][self.col + 1].is_barrier(): # upper right
    # 		self.neighbors.append(grid[self.row -1][self.col + 1])
    # 	if self.row < self.total_rows - 1 and self.col < self.total_rows - 1 and not grid[self.row + 1][self.col + 1].is_barrier(): # lower right
    # 		self.neighbors.append(grid[self.row + 1][self.col + 1])

    def __lt__(self, other):
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def reconstruct_path(came_from, current, draw):
    go_to = [current]
    while current in came_from:
        current = came_from[current]
        go_to.append(current)
        current.make_path()
        draw()
    return go_to


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start}
    fail = []
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        fail.append(current)
        open_set_hash.remove(current)
        if current == end:
            go_to = reconstruct_path(came_from, end, draw)
            end.make_end()
            return True, go_to
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current != start:
            current.make_closed()
    Tk().wm_withdraw()
    messagebox.showinfo("error", "no solution")
    return False, fail


# def algorithm(draw, grid, start, end):
# 	count = 0
# 	a_Queue = PriorityQueue()
# 	a_Queue.put((0, count, start))
# 	check_overdrive = {start}
# 	came_from = {}
# 	g = {spot: 0 for row in grid for spot in row}
# 	g[start] = 0
# 	f = {spot: 0 for row in grid for spot in row}
# 	f[start] = h(start.get_pos(), end.get_pos())
# 	while not a_Queue.empty():
# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 		current = a_Queue.get()[2]
# 		#check_overdrive.remove(current)
# 		if current == end:
# 			# reconstruct_path(came_from, end, draw)
# 			# end.make_end()
# 			return True
# 		for idx, neighbor in enumerate(current.neighbors):
# 			came_from[neighbor] = current
# 			if 0 <= idx and idx < 4:
# 				g[neighbor] = g[current]+1
# 			else:
# 				g[neighbor] = g[current] + math.sqrt(2)
# 			f[neighbor] = g[neighbor] + h(neighbor.get_pos(), end.get_pos())
# 			if neighbor not in check_overdrive:
# 				count += 1
# 				a_Queue.put((f[neighbor], count, neighbor))
# 				check_overdrive.add(neighbor)
# 				neighbor.make_open()
# 		draw()
# 		if current != start:
# 			current.make_closed()
#
# 	return False

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def draw_car(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def path_line(go_to, ROWS, width):
    distance_scale = (width//ROWS)//4
    start_point = go_to[len(go_to) - 1]
    s = []
    action = []
    for i in range(len(go_to)):
        s.append(go_to[-(i+1)])
    for i in range(len(s)-1):
        if s[i+1].get_pos()[0] - s[i].get_pos()[0] == 1: #RIGHT
            for j in range(distance_scale):
                action.append(1)
        if s[i+1].get_pos()[0] - s[i].get_pos()[0] == -1: #LEFT
            for j in range(distance_scale):
                action.append(2)
        if s[i+1].get_pos()[1] - s[i].get_pos()[1] == 1: #DOWN
            for j in range(distance_scale):
                action.append(3)
        if s[i+1].get_pos()[1] - s[i].get_pos()[1] == -1: #UP
            for j in range(distance_scale):
                action.append(4)
    return action, start_point

def run_car(draw_car, action, start_point, animation, win, ROWS, width):
    x, y = start_point.get_pos()
    x = x*(width//ROWS)
    y = y*(width//ROWS)
    win.blit(animation[3], (x, y))
    idx = 0
    while idx < len(action):
        clock.tick(10)
        draw_car()
        if action[idx] == 1:
            x += 4
            win.blit(animation[3], (x, y))
        if action[idx] == 2:
            x -= 4
            win.blit(animation[2], (x, y))
        if action[idx] == 3:
            y += 4
            win.blit(animation[1], (x, y))
        if action[idx] == 4:
            y -= 4
            win.blit(animation[0], (x, y))
        idx += 1
        pygame.display.update()


def main(win, width):
    ROWS = 50

    size = random.randint(ROWS * ROWS / 2 - 100, ROWS * ROWS / 2)
    random_map = []

    image = pygame.transform.scale(pygame.image.load('white_car1.png'), (width // ROWS, width // ROWS))
    car_right = pygame.transform.rotate(image, 270)
    car_up = pygame.transform.rotate(image, 0)
    car_left = pygame.transform.rotate(image, 90)
    car_down = pygame.transform.rotate(image, 180)
    animation = [car_up, car_down, car_left, car_right]

    for i in range(size):
        y = random.randint(0, 49)
        x = random.randint(0, 49)
        random_map.append([y, x])
    grid = make_grid(ROWS, width)
    random_check = False
    start = None
    end = None
    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:  # LEFT
                random_check = True
                pos = pygame.mouse.get_pos()
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
            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and random_check == False:
                    random_check = True
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
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    start_run, go_to = algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    action, start_point = path_line(go_to, ROWS, width)
                if event.key == pygame.K_r and start_run == True:
                    run_car(lambda: draw_car(win, grid, ROWS, width), action, start_point, animation, win, ROWS, width)
                if event.key == pygame.K_c:
                    random_check = False
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    pygame.quit()

if __name__ == '__main__':
    main(WIN, WIDTH)
