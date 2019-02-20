import pygame
import random

pygame.init()
width = 1000
height = 500
count = 0
sound_2 = pygame.mixer.Sound('shot_sound.wav')

white = 255, 255, 255
screen = pygame.display.set_mode((width, height))
bg_img = pygame.image.load("background.png")
gun = pygame.image.load("gun_1.png")
aim=pygame.image.load("aim_pointer.png")
zombieList=[]
gun_y=height -200
text1=0
red = 255,0,0

for i in range(4):

     zom_img = pygame.image.load("zombie_{}.png".format(i+1))
     zombieList.append(zom_img)


zombieImage=random.choice(zombieList)
zombieHeight= zombieImage.get_height()
zombieWidth=zombieImage.get_width()
randomx = random.randrange(0, width - zombieWidth)
randomy = random.randrange(0, height - zombieHeight)
clock = pygame.time.Clock()
FPS = 90

def gameover():
    font = pygame.font.SysFont(None, 50)
    text = font.render("game over", True, white)
    screen.blit(text, (200, 200))
def score(c):
    font = pygame.font.SysFont(None, 50)
    text1 = font.render("score=" + str(c), True, white)
    screen.blit(text1, (0, 0))
    return text1

game = True
while game:
    for event in pygame.event.get():
        text1=score(count)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_1.colliderect(rect_2):
                zombieImage = random.choice(zombieList)
                randomx = random.randrange(0, width - zombieWidth)
                randomy = random.randrange(0, height - zombieHeight)
                count += 1
                sound_2.play()

    pos_x,pos_y=pygame.mouse.get_pos()
    screen.blit(bg_img, (0, 0))
    screen.blit(zombieImage,(randomx, randomy))
    screen.blit(aim,(pos_x-aim.get_width()/2 , pos_y-aim.get_height()/2))
    screen.blit(gun, (pos_x-aim.get_width()/2 , pos_y-aim.get_height()/2))
    screen.blit(text1, (0, 0))
    rect_1=pygame.Rect(pos_x,pos_y,aim.get_width() , aim.get_height())
    rect_2=pygame.Rect(randomx,randomy,zombieImage.get_width() , zombieImage.get_height())
    pygame.display.update()
    clock.tick(FPS)