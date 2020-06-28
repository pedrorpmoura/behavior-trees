import pygame
import random
import sys
import math


import out

width = 512
height = 512

FREE = 0
WALL = 1
PLAYER = 2
BALL = 3

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"


def position_inside_borders(p, board):
    if p[0] < 0 or p[0] > board.size - 1 or p[1] < 0 or p[1] > board.size - 1:
        return False
    
    return True

def position_is_valid(p, board):
    if p[0] < 0 or p[0] > board.size - 1 or p[1] < 0 or p[1] > board.size - 1:
        return False
    
    if board.structure[p] != FREE:
        return False

    return True


def cross_product(a,b):
    return a[0] * b[1] - a[1] * b[0]

def dot_product(a,b):
    return a[0] * b[0] + a[1] * b[1]


def collinear_same_direction(a,b):
    return cross_product(a,b) == 0 and dot_product(a,b) > 0

class Board:
    
    def __init__(self, size):
        self.size = size
        self.structure = { (x,y): FREE for x in range(size) for y in range(size) }
    

    def setup(self):
        self.create_walls(8)
        self.create_ball()

    def create_walls(self, n_walls):
        min_wall_size = 3
        max_wall_size = 5

        for w in range(n_walls):
            wall_size = random.randint(min_wall_size, max_wall_size)
            orientation = random.randint(0,1)
            position = random.choice(list(self.structure.keys()))

            wall = self.create_wall(wall_size, orientation, position)

            while not self.wall_is_valid(wall):
                wall_size = random.randint(min_wall_size, max_wall_size)
                orientation = random.randint(0,1)
                position = random.choice(list(self.structure.keys()))

                wall = self.create_wall(wall_size, orientation, position)
            
            self.add_wall(wall)
            
    
    def create_wall(self, wall_size, orientation, position):
        wall = []
        x = position[0]
        y = position[1]
        for i in range(wall_size):
            if orientation == 0:
                wall.append((x, y + i))
            else:
                wall.append((x + i, y))
        
        return wall


    def wall_is_valid(self, wall):
        for p in wall:
            if not position_is_valid(p, self):
                return False

        return True


    def add_wall(self, wall):
        for p in wall:
            self.structure[p] = WALL


    def create_ball(self):
        position = random.choice(list(self.structure.keys()))
        while not position_is_valid(position, self):
            position = random.choice(list(self.structure.keys()))

        self.ball = position
        self.structure[position] = BALL
    

    def render(self, screen):
        n = width / self.size
    
        for (x,y) in list(self.structure.keys()):
            if self.structure[(x,y)] == WALL:
                color = (0,0,0)
            elif self.structure[(x,y)] == BALL:
                color = (255,0,0)
            elif (x + y) % 2 == 0:
                color = (112,128,144)
            else:
                color = (119,136,153)

            pygame.draw.rect(screen, color, (x * n, y * n, n, n))
    





class Player:
    
    def __init__(self, board):
        self.board = board
    

    def setup(self):
        structure = self.board.structure
        self.position = random.choice(list(structure.keys()))
        while not position_is_valid(self.position, self.board):
            self.position = random.choice(list(structure.keys()))
        
        self.create_fov(self.board)
        self.shortest_path = self.find_shortest_path(self.position, self.board.ball)
        self.ball_found = self.ball_in_fov()
        self.ball_grabbed = False
        self.ball_within_reach = self.ball_is_within_reach()    

    def create_fov(self, board, fov_distance = 4):
        x = self.position[0]
        y = self.position[1]
        self.fov = set()
        for (x0,y0), state in board.structure.items():
            d = math.sqrt((x0 - x)**2 + (y0 - y)**2)
            if d <= fov_distance and state != WALL and (x,y) != (x0,y0):
                self.fov.add(((x0,y0), state))
        
        points_for_removal = set()
        #for (x0, y0), state in self.fov:
        #    if state == WALL:
        #        a = (x0 - x, y0 - ycr)
        #        da = math.sqrt(a[0]**2 + a[1]**2)
#
        #        for (x1,y1), state in self.fov:
        #            if state == FREE or state == BALL:
        #                b = (x1 - x, y1 - y)
        #                db = math.sqrt(b[0]**2 + b[1]**2)
        #                if collinear_same_direction(a,b) and db > da:
        #                    points_for_removal.add(((x1,y1), state))
        #                    
        #                    #self.fov.remove(((x1,y1), state))
        
        self.fov = dict(self.fov.difference(points_for_removal))
        self.shortest_path = self.find_shortest_path(self.position, self.board.ball)
        print(self.find_shortest_path(self.position, self.board.ball))


    def ball_in_fov(self):
        return len(self.shortest_path) > 1


    def ball_is_within_reach(self):
        x = self.position[0]
        y = self.position[1]
        for i in [-1,1]:
            if position_inside_borders((x + i, y), self.board) and self.board.structure[(x + i, y)] == BALL:
                return True
            
            if position_inside_borders((x, y + i), self.board) and self.board.structure[(x, y + i)] == BALL:
                return True
        
        return False
                    

    def grab_ball(self):
        if self.ball_within_reach:
            self.ball_grabbed = True
            self.board.structure[self.board.ball] = FREE
            print("Ball grabbed")


    def find_adjacents(self, position, d):
        adjacents = set()

        x,y = position
        if (x+1,y) in d:
            adjacents.add((x+1,y))

        if (x-1,y) in d:
            adjacents.add((x-1,y))

        if (x,y+1) in d:
            adjacents.add((x,y+1))

        if (x,y-1) in d:
            adjacents.add((x,y-1))

        return adjacents
    
    def get_adjacency_list(self, d):
        adj = {}
        for p in d:
            adj[p] = self.find_adjacents(p, d)
    
        return adj

    def bfs(self, position, adj):
        parent = {}
        discovered = [] 
        queue = []
        discovered.append(position)
        queue.append(position) 
        while queue:
            c = queue.pop(0) 
            for n in adj[c]:
                if n not in discovered: 
                    discovered.append(n) 
                    parent[n] = c 
                    queue.append(n)
            
        return parent
    

    def find_shortest_path(self, src, dest):

        aux = self.fov
        aux[self.position] = PLAYER
        adj = self.get_adjacency_list(aux)
        path = []
        if dest in adj:
            parent = self.bfs(src, adj)
            
            path.append(dest)
            while dest in parent:
                dest = parent[dest]
                path.insert(0, dest)

        return path


    def approach_ball(self):
        self.position = self.shortest_path.pop(0)
        self.ball_within_reach = self.ball_is_within_reach()
        


    def search_ball(self):
        x = self.position[0]
        y = self.position[1]

        i = random.choice([1,-1])
        j = random.randint(0,3)

        if j == 0:
            if position_is_valid((x + i, y), self.board):
                self.position = (x + i, y)
        else:
            if position_is_valid((x, y + i), self.board):
                self.position = (x, y + i)

        self.create_fov(self.board)
        self.shortest_path = self.find_shortest_path(self.position, self.board.ball)
        self.ball_found = self.ball_in_fov()
        if self.ball_found:
            self.fov = {}
        self.ball_within_reach = self.ball_is_within_reach()
        

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("pressed left key")
                self.move_player(LEFT)
            elif event.key == pygame.K_RIGHT:
                print("pressed right key")
                self.move_player(RIGHT)
            elif event.key == pygame.K_UP:
                print("pressed up key")
                self.move_player(UP)
            elif event.key == pygame.K_DOWN:
                print("pressed down key")
                self.move_player(DOWN)
            elif event.key == pygame.K_SPACE:
                print("pressed space key")
                if not self.ball_grabbed:
                    self.grab_ball()


    def move_player(self, move):
        x = self.position[0]
        y = self.position[1]
        if move == UP and position_is_valid((x, y-1), self.board):
            y = y - 1
        elif move == DOWN and position_is_valid((x, y+1), self.board):
            y = y + 1
        elif move == RIGHT and position_is_valid((x+1, y), self.board):
            x = x + 1
        elif move == LEFT and position_is_valid((x-1, y), self.board):
            x = x - 1

        self.position = (x,y)
        self.create_fov(self.board)
        self.shortest_path = self.find_shortest_path(self.position, self.board.ball)
        self.ball_found = self.ball_in_fov()
        if self.ball_found:
            print("ball found")
        
        self.ball_within_reach = self.ball_is_within_reach()
        if self.ball_within_reach:
            print("ball within reach")



    def render(self, screen):
        n = width / self.board.size

        color = (0,0,255)
        x = self.position[0]
        y = self.position[1]

        pygame.draw.rect(screen, color, (x * n, y * n, n, n))
        if self.ball_grabbed:
            pygame.draw.rect(screen, (255,0,0), (x * n + (n/4), y*n + (n/4) ,n/2, n/2))


        # draw fov
        color = (0,255,0)
        for (x0,y0) in list(self.fov.keys()):
            rect = pygame.Surface((n, n))
            rect.set_alpha(50)
            rect.fill(color)
            screen.blit(rect, (x0 * n, y0 * n))
        
        for (x0,y0) in self.shortest_path:
            color = (255, 0, 0)
            rect = pygame.Surface((n, n))
            rect.set_alpha(50)
            rect.fill(color)
            screen.blit(rect, (x0 * n, y0 * n))




class Game:
    
    def __init__(self):
        self.board = Board(16)
        self.player = Player(self.board)
        pass 

    def setup(self):
        self.board.setup()
        self.player.setup()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            else:
                self.player.process_event(event)
        

    def update(self, clock, time):
        clock.tick(time)


    def render(self, screen):
        self.board.render(screen)
        self.player.render(screen)



def main():
    pygame.init()

    screen = pygame.display.set_mode((width,height))

    pygame.display.set_caption("GAME")

    pygame.time.delay(100)
    clock = pygame.time.Clock()

    game = Game()
    game.setup()
    S = out.Simulator(game.player)

    game.render(screen)
    
    while True:
        
        game.process_events()

        S.tick()
        game.update(clock, 2)
        game.render(screen)

        pygame.display.update()
        


if __name__ == "__main__":
    main()