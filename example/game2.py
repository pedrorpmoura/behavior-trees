import pygame
import random
import sys

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


def position_is_valid(p, board):
    if p[0] < 1 or p[0] > board.size - 2 or p[1] < 1 or p[1] > board.size - 2:
        return False
    
    if board.structure[p] != FREE:
        return False

    return True



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
        pass


    def move_player(self, move):
        x = self.position[0]
        y = self.position[1]
        if move == UP:
            y = y - 1
        elif move == DOWN:
            y = y + 1
        elif move == RIGHT:
            x = x + 1
        elif move == LEFT:
            x = x - 1

        self.position = (x,y)

    def render(self, screen):
        n = width / self.board.size

        color = (0,0,255)
        x = self.position[0]
        y = self.position[1]
        pygame.draw.rect(screen, color, (x * n, y * n, n, n))

    
    
           
    




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

    game.render(screen)
    
    while True:
        
        game.process_events()
        game.update(clock, 30)
        game.render(screen)

        pygame.display.update()
        


if __name__ == "__main__":
    main()