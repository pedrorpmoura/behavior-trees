import pygame
pygame.init()

width = 500
height = 500


def draw_grid(screen, N):
    n = N / width

    for i in range(N):
        for j in range(N):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, (255, 0, 0), (i, j, i*n, j*n))

screen = pygame.display.set_mode((width,height))
screen.fill((0,0,0))

pygame.display.set_caption("PAC-MAN")

pygame.time.delay(100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid(screen, 10)
    pygame.display.update()
