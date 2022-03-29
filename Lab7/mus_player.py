# from curses import KEY_ENTER
import os
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("music")
pygame.mixer.init()

music_bg = 'D:\pp\pp2\Lab7\musics\images\\ФОН.jpg'
controls_images = 'D:\pp\pp2\Lab7\musics\images\пауза.png'
font_obj = pygame.font.SysFont('simsun', 25) # Шрифт




def true_name(name):
    new_name = ''
    for i in name:
        if i == '.':
            return new_name
        new_name = new_name + i

def draw_song_name(music):
    wbk_obj = font_obj.render(true_name(str(music)), True, (0, 255, 255))
    k_obj = wbk_obj.get_rect()
    k_obj.center = (400, 570)
    screen.blit(wbk_obj, k_obj)
    pygame.display.update()

def draw_song_photo(music):
    images = 'D:\pp\pp2\Lab7\musics\images\\' + true_name(str(music)) + '.jpg'
    im = pygame.image.load(images)
    screen.blit(im, (170, 50))
    pygame.display.update()
    
path = 'D:\pp\pp2\Lab7\musics'
musics = [ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ]

def sing_a_song(musics, i):
    pygame.mixer.music.load('D:\pp\pp2\Lab7\musics\\'+str(musics[i]))
    pygame.mixer.music.play()
    

i = 0
pause = False
while True:
    STOPPED_PLAYING = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(STOPPED_PLAYING)
    bg = pygame.image.load(music_bg)
    screen.blit(bg, (0, 0))
    contr = pygame.image.load(controls_images)
    screen.blit(contr, (-2, 29))
    if pygame.mixer.music.get_busy() == 1:
        is_sing = True
    else:
        is_sing = False
    
    # Если не играет музыка
    if  is_sing == False:
        sing_a_song(musics, i)
        draw_song_name(musics[i])
        draw_song_photo(musics[i])
        is_sing = not is_sing
    # Если музыка играет
    else:
        # отображение названия песни
        draw_song_name(musics[i])
        draw_song_photo(musics[i])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if STOPPED_PLAYING == event.type:
            i = i + 1
            if i > 7:
                i = 0
            c_music = sing_a_song(musics, i)
            draw_song_name(musics[i])
            draw_song_photo(musics[i])
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            # print(x, y)
            if x > 307 and x < 347 and y > 523 and y < 543:
                i = i - 1
                if i < 0:
                    i = 7
                c_music = sing_a_song(musics, i)
                draw_song_name(musics[i])
                draw_song_photo(musics[i])
                print("Нажата предыдущую песня")
            if x > 455 and x < 495 and y > 523 and y < 543:
                i = i + 1
                if i > 7:
                    i = 0
                c_music = sing_a_song(musics, i)
                draw_song_name(musics[i])
                draw_song_photo(musics[i])
                print('Щелкнул следущую песню')
            if x > 371 and x < 391 and y > 523 and y < 543:
                pause = True
            if x > 406 and x < 436 and y > 523 and y < 543:
                pause = False

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                i = i + 1
                if i > 7:
                    i = 0
                c_music = sing_a_song(musics, i)
                draw_song_name(musics[i])
                draw_song_photo(musics[i])
                print('Щелкнул следущую песню')    
            if event.key == K_LEFT:
                i = i - 1
                if i < 0:
                    i = 7
                c_music = sing_a_song(musics, i)
                draw_song_name(musics[i])
                draw_song_photo(musics[i])
                print("Нажата следующая песня")
    if pause:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
            
    pygame.display.update()