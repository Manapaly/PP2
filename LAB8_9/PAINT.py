import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    bg = pygame.image.load("D:\pp\pp2\Lab8\images\MAIN_PAINT.png")
    bg = pygame.transform.scale(bg, (800, 600))
    lg = pygame.image.load("D:\pp\pp2\Lab8\images\MAIN_PAINT2.png")
    lg = pygame.transform.scale(lg, (64, 600))

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    screen.blit(bg,(0,0))
    
    prevX = 0
    prevY = 0

    isMouseDown = False
    op = False
    ip = False
    line = False
    Rect = False
    Erase = False
    Circle = False
    Triangle = False
    Right_Triangle = False
    Romb = False
    SQUARE = False

    COLOR = BLACK
    currentX = 1 
    prevX = 1
    currentY = 1
    prevY = 1

    while True:
        screen.blit(lg, (0, 0))
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.pos[0] > 13 and event.pos[0] < 56 and event.pos[1] > 174 and event.pos[1] < 206 :
                    COLOR = BLACK
                if event.pos[0] > 13 and event.pos[0] < 56 and event.pos[1] > 217 and event.pos[1] < 255 :
                    COLOR = WHITE
                if event.pos[0] > 13 and event.pos[0] < 56 and event.pos[1] > 260 and event.pos[1] < 296 :
                    COLOR = RED
                if event.pos[0] > 13 and event.pos[0] < 56 and event.pos[1] > 301 and event.pos[1] < 345 :
                    COLOR = GREEN
                if event.pos[0] > 13 and event.pos[0] < 56 and event.pos[1] > 348 and event.pos[1] < 391 :
                    COLOR = BLUE
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if event.pos[0] > 7 and event.pos[0] < 53 and event.pos[1] > 58 and event.pos[1] < 96 :
                    line = True
                    Rect = False
                    Erase = False
                    Circle = False
                    Triangle = False
                    Right_Triangle = False
                    Romb = False
                    SQUARE = False
                if event.pos[0] > 13 and event.pos[0] < 56 and event.pos[1] > 102 and event.pos[1] < 129 :
                    line = False
                    Rect = True
                    Erase = False
                    Circle = False
                    Triangle = False
                    Right_Triangle = False
                    Romb = False
                    SQUARE = False
                if event.pos[0] > 7 and event.pos[0] < 53 and event.pos[1] > 8 and event.pos[1] < 58 :
                    line = False
                    Rect = False
                    Erase = True
                    Circle = False
                    Triangle = False
                    Right_Triangle = False
                    Romb = False
                    SQUARE = False
                if event.pos[0] > 7 and event.pos[0] < 53 and event.pos[1] > 134 and event.pos[1] < 170 :
                    line = False
                    Rect = False
                    Erase = False
                    Circle = True
                    Triangle = False
                    Right_Triangle = False
                    Romb = False
                    SQUARE = False
                if event.pos[0] > 7 and event.pos[0] < 53 and event.pos[1] > 397 and event.pos[1] < 443 :
                    line = False
                    Rect = False
                    Erase = False
                    Circle = False
                    Triangle = True
                    Right_Triangle = False
                    Romb = False
                    SQUARE = False
                if event.pos[0] > 7 and event.pos[0] < 53 and event.pos[1] > 448 and event.pos[1] < 492 :
                    line = False
                    Rect = False
                    Erase = False
                    Circle = False
                    Triangle = False
                    Right_Triangle = True
                    Romb = False
                    SQUARE = False
                if event.pos[0] > 7 and event.pos[0] < 53 and event.pos[1] > 495 and event.pos[1] < 547 :
                    line = False
                    Rect = False
                    Erase = False
                    Circle = False
                    Triangle = False
                    Right_Triangle = False
                    Romb = True
                    SQUARE = False
                if event.pos[0] > 7 and event.pos[0] < 53 and event.pos[1] > 550 and event.pos[1] < 595 :
                    line = False
                    Rect = False
                    Erase = False
                    Circle = False
                    Triangle = False
                    Right_Triangle = False
                    Romb = False
                    SQUARE = True

                
            if line:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        isMouseDown = True
                        prevX = event.pos[0]
                        prevY = event.pos[1]
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1: 
                        isMouseDown = False
                if event.type == pygame.MOUSEMOTION:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
                if isMouseDown :
                    pygame.draw.line(screen, COLOR, (prevX, prevY), (currentX, currentY))
            if Rect:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    op = True
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    current_pos = pygame.mouse.get_pos() 
                    ip = True 
                if pos[0] < 62 or current_pos[0] < 62:
                    ip = False 
                if op and ip:
                    pygame.draw.rect(screen, COLOR, (pos[0], pos[1], current_pos[0] - pos[0], current_pos[1]- pos[1]), 1)
                    ip = False
                    op = False
            if Erase:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        isMouseDown = True
                        prevX = event.pos[0]
                        prevY = event.pos[1]
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1: 
                        isMouseDown = False
                if event.type == pygame.MOUSEMOTION:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
                if isMouseDown :
                    pygame.draw.line(screen, WHITE, (prevX, prevY), (currentX, currentY), 25)
            if Circle:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    op = True
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    current_pos = pygame.mouse.get_pos() 
                    ip = True 
                if pos[0] < 62 or current_pos[0] < 62:
                    ip = False 
                if op and ip:
                    pygame.draw.circle(screen, COLOR, ((current_pos[0] + pos[0])/2,  (current_pos[1] + pos[1])/2), (current_pos[1] - pos[1])/2, 1)
                    ip = False
                    op = False
            if Triangle:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    op = True
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    current_pos = pygame.mouse.get_pos() 
                    ip = True 
                if pos[0] < 62 or current_pos[0] < 62:
                    ip = False 
                if op and ip:
                    pygame.draw.lines(screen, COLOR, True,[[pos[0], pos[1]], [pos[0], current_pos[1]], [current_pos[0], current_pos[1]]], 2)
                    ip = False
                    op = False
            if Right_Triangle:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    op = True
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    current_pos = pygame.mouse.get_pos() 
                    ip = True 
                if pos[0] < 62 or current_pos[0] < 62:
                    ip = False 
                if op and ip:
                    pygame.draw.lines(screen, COLOR, True,[[pos[0] + (current_pos[0] - pos[0])/2 , pos[1]], [pos[0], current_pos[1]], [current_pos[0], current_pos[1]]], 2)
                    ip = False
                    op = False
            if Romb:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    op = True
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    current_pos = pygame.mouse.get_pos() 
                    ip = True 
                if pos[0] < 62 or current_pos[0] < 62:
                    ip = False 
                if op and ip:
                    pygame.draw.lines(screen, COLOR, True,[[pos[0] + (current_pos[0] - pos[0])/2 , pos[1]], [pos[0], pos[1] + (current_pos[1] - pos[1])/2], [pos[0] + (current_pos[0] - pos[0])/2 , current_pos[1]], [current_pos[0], pos[1] + (current_pos[1] - pos[1])/2]], 2)
                    ip = False
                    op = False
            if SQUARE:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    op = True
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    current_pos = pygame.mouse.get_pos() 
                    ip = True 
                if pos[0] < 62 or current_pos[0] < 62:
                    ip = False 
                if op and ip:
                    pygame.draw.rect(screen, COLOR, (pos[0], pos[1], current_pos[1] - pos[1], current_pos[1] - pos[1]), 1)
                    ip = False
                    op = False

            
        prevX = currentX
        prevY = currentY
        
        pygame.display.flip()
        clock.tick(60)

main()