import os, random
import sys
import pygame

pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 10
ENEMTY_STEP = 6
COIN_STEP = 6

BLACK = (0, 0, 0)

SCORE  = 1
COINES = 0
clock = pygame.time.Clock()

score_font = pygame.font.SysFont("Verdana", 20)

SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer")

bg = pygame.image.load("D:\pp\pp2\Lab8\images\AnimatedStreet.png")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("D:\pp\pp2\Lab8\images\Enemy.png")
        self.rect = self.image.get_rect()
        self.sss = random.randint(40, SCREEN_WIDTH - 40)
        self.rect.center = (self.sss, 0)

    def update(self):
        global SCORE
        global COINES
        global ENEMTY_STEP
        self.rect.move_ip(0, ENEMTY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)
            if SCORE % 8 == 0:
                ENEMTY_STEP += 2

    def draw(self, surface):
        surface.blit(self.image, self.rect)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("D:\pp\pp2\Lab8\images\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.coin = random.choice(os.listdir("D:\pp\pp2\Lab8\coins\\"))
        self.image = pygame.image.load("D:\pp\pp2\Lab8\coins\\" + self.coin)
     
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def update(self):
        global COINES
        self.rect.move_ip(0, COIN_STEP)
        
        if pygame.sprite.spritecollideany(P1, coins):
            COINES += int(str(self.coin[0:len(self.coin)-4]))
            self.coin = random.choice(os.listdir("D:\pp\pp2\Lab8\coins\\"))
            self.image = pygame.image.load("D:\pp\pp2\Lab8\coins\\" + self.coin)
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0) 
        if(self.rect.bottom > SCREEN_HEIGHT):
            a = random.choice(os.listdir("D:\pp\pp2\Lab8\coins\\"))
            self.image = pygame.image.load("D:\pp\pp2\Lab8\coins\\" + a)
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
C1 = Coin()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(E1)
coins.add(C1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()
    C1.update()
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.quit()
        sys.exit()
    if pygame.sprite.spritecollideany(C1, enemies):
        C1.update()
    
        
    SURF.blit(bg, (0, 0))

    E1.draw(SURF)
    P1.draw(SURF)
    C1.draw(SURF)

    score_img = score_font.render(str(SCORE), True, BLACK) 
    coins_img = score_font.render(str(COINES), True, BLACK)
    
    SURF.blit(score_img, (10, 10))
    SURF.blit(coins_img,(350,10))

    pygame.display.update()
    clock.tick(FPS)