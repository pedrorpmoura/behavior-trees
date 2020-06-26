import pygame
import random
import math

width = 512
height = 512


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y



def generate_wall(size, orientation, position):
    wall = []

    x = position[0]
    y = position[1]
    for i in range(size):
        if orientation == 0:
            wall.append((x, y + i))
        else:
            wall.append((x + i, y))
    
    return wall


def wall_is_valid(wall, map_dict):
    N = int(math.sqrt(len(map_dict)))
    for p in wall:
        if p[0] < 1 or p[0] > N - 2 or p[1] < 1 or p[1] > N - 2:
            return False

        elif map_dict[p] != 0:
            return False

    return True


def add_wall(wall, map_dict):
    for p in wall:
        map_dict[p] = 1

def generate_walls(n_walls, map_dict):
    min_wall_size = 3
    max_wall_size = 5

    for w in range(n_walls):
        wall_size = random.randint(min_wall_size, max_wall_size)

        # orientation: 0 - Horizontal, 1 - Vertical
        orientation = random.randint(0,1)

        # choose random position to create wall
        pos = random.choice(list(map_dict.keys()))

        wall = generate_wall(wall_size, orientation, pos)

        while not wall_is_valid(wall, map_dict):
            wall_size = random.randint(min_wall_size, max_wall_size)
            orientation = random.randint(0,1)
            pos = random.choice(list(map_dict.keys()))

            wall = generate_wall(wall_size, orientation, pos)
        
        
        add_wall(wall, map_dict)


def pos_valid(pos, map_dict):
    N = int(math.sqrt(len(map_dict)))
    if pos[0] < 1 or pos[0] > N - 2 or pos[1] < 1 or pos[1] > N - 2:
        return False

    elif map_dict[pos]:
        return False

    return True

def generate_ball(map_dict):
    
    pos = random.choice(list(map_dict.keys()))

    while not pos_valid(pos, map_dict):
        pos = random.choice(list(map_dict.keys()))

    map_dict[pos] = 2



def create_map(N):
    d = { (i,j) : 0 for i in range(N) for j in range(N) }

    generate_walls(8, d)
    generate_ball(d)

    return d


def draw_map(map_dict, screen, N):
    n = width / N
    
    for (x,y) in list(map_dict.keys()):

        if map_dict[(x,y)] == 1:
            color = (0,0,0)
        elif map_dict[(x,y)] == 2:
            color = (255,0,0)
        elif map_dict[(x,y)] == 3:
            color = (0,0,255)
        elif (x + y) % 2 == 0:
            color = (112,128,144)
        else:
            color = (119,136,153)

        pygame.draw.rect(screen, color, (x * n, y * n, n, n))
    



def main():
    pygame.init()

    screen = pygame.display.set_mode((width,height))

    pygame.display.set_caption("GAME")

    pygame.time.delay(100)

    N = 16
    game_dict = create_map(N)
    draw_map(game_dict, screen, N)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()





if __name__ == "__main__":
    main()