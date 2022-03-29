import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ПОЧТИ ИГРА")
w, h = screen.get_size()

done = False
is_open = True

x = random.randint(0, 800-20)
y = random.randint(0, 600-20)
dx = 0
dy = 0
step = 20

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_open = not is_open
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        dx = 1
                        dy = 0
                    if event.key == pygame.K_LEFT:
                        dx = -1
                        dy = 0
                    if event.key == pygame.K_UP:
                        dx = 0
                        dy = -1
                    if event.key == pygame.K_DOWN:
                        dx = 0
                        dy = 1
        if is_open:
            e = 5
        else:
            e = 0
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        color = (a, b, c)

        screen.fill((255,255,255))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600), 5)
        pygame.draw.circle(screen, color, (x, y), 25, e)
        x += step * dx
        y += step * dy
        if x < 0 + step:
            x -= step * dx
        if x > w - 20:
            x -=step * dx
        if y < 0 + step:
            y -= step * dy
        if y > h - 20:
            y -=step * dy
    
        pygame.display.flip()
        clock.tick(10)
        dx = 0
        dy = 0