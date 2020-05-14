import pygame
import random

width = 512
height = 512


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y



def draw_grid(screen, N):
    n = width / N
    
    for i in range(N):
        for j in range(N):
            
            p = random.randint(0,1)
            if p == 0:
                color = (51, 102, 0)
            elif p == 1:
                color = (0, 102, 0)
            
            pygame.draw.rect(screen, color, (i * n, j * n, n, n))

    return n


def draw_house(screen, n):

    for i in range(5, 12):
        pygame.draw.rect(screen, (0,0,0), (i * n, 2 * n, n, n))

def main():
    pygame.init()

    screen = pygame.display.set_mode((width,height))

    pygame.display.set_caption("PAC-MAN")

    pygame.time.delay(100)

    n = draw_grid(screen, 16)

    draw_house(screen, n)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        

        pygame.display.update()


if __name__ == "__main__":
    main()