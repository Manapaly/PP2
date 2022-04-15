
from os import scandir
from select import select
import pygame
import random
import sys
import time



pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE= (0, 0, 255)
LINE_COLOR = (50, 50, 50)
HEIGHT = 800
WIDTH = 800

SCORE=0
LEVEL=0
FPS=5
BLOCK_SIZE = 20
list_x = []
list_y = []
score_font = pygame.font.SysFont('Verdana', 28)
level_font = pygame.font.SysFont('Verdana', 28)

COLOR = [(255,0,0),(0,255,0),(0,0,255),(120,120,120),(77,48,49),(14,48,199)]
class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
# qq = random.randint(0,5)
class Food:
    def __init__(self):
        self.location = Point(4, 10)

    def draw(self,qq):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, COLOR[qq], rect)

    def respawn(self):
        self.location.x = random.randint(0,  19)
        self.location.y = random.randint(0,  19)
    

qq = 1
cnt = 0
lev = 7
class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0

        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE

        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE




    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect( SCREEN, (255, 0, 0), rect)

        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect( SCREEN, (0, 255, 0), rect)



    
    def check_collision(self, food):
        global SCORE, FPS, LEVEL, qq, cnt,lev, list_x, list_y
        # print(len(self.body))
        # print(food.location.x)
        # print()
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                list_x.append(food.location.x)
                list_y.append(food.location.y)
                if qq == 0:
                    SCORE+=1
                if qq == 1:
                    SCORE+=2
                if qq == 2:
                    SCORE+=3
                if qq == 3:
                    SCORE+=4
                if qq == 4:
                    SCORE+=5
                if qq == 5:
                    SCORE+=6
                
                qq = random.randint(0,5)
                if SCORE >= lev :
                    LEVEL+=1
                    lev = lev + 7
                    FPS+=5
                food.respawn()
    def game_over(self):
        global list_x, list_y
        if self.body[0].x in list_x:
            if self.body[0].y in list_y:
                return True


def main():

    global SCREEN, CLOCK, SCORE, FPS, LEVEL, cnt
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    game_end = pygame.image.load("D:\pp\pp2\Lab8\images\game_over.jpg")
    ge = pygame.transform.scale(game_end, (800, 800))

    snake = Snake()
    food = Food()
    ok_x1 = True
    ok_x2 = True
    ok_y = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and ok_x1 and ok_x2:
                    ok_x1 = False
                    ok_x2 = True
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT and ok_x1 and ok_x2:
                    ok_x1 = True
                    ok_x2 = False
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    ok_x1 = True
                    ok_x2 = True
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    ok_x1 = True
                    ok_x2 = True
                    snake.dx = 0
                    snake.dy = 1

    

        snake.move()
        snake.check_collision(food)
        
            # time.sleep(5)
            # pygame.quit()
        score_img = score_font.render( str(SCORE), True, WHITE)
        level_img = level_font.render( str(LEVEL), True, WHITE)


        SCREEN.fill(BLACK)
        SCREEN.blit(score_img, (10, 10))
        SCREEN.blit(level_img, (140, 10))
        global qq
        snake.draw()
        food.draw(qq)

        # drawGrid()
        if snake.game_over():
            SCREEN.blit(ge, (0, 0))
            
        pygame.display.update()

        CLOCK.tick(FPS)







def drawGrid():

    for x in range(0, WIDTH, BLOCK_SIZE):

        for y in range(0, HEIGHT, BLOCK_SIZE):

            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)







main()
