import pygame
import time
win_width = 600
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
background = pygame.transform.scale(pygame.image.load('bgr.jpg'), (win_width, win_height))
pygame.mixer.init()
pygame.mixer.music.load('brgr.ogg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
ssound = pygame.mixer.Sound('Rocket.ogg')
msound = pygame.mixer.Sound('Miss.ogg')
game = True
finish = False
clock = pygame.time.Clock()
FPS = 90

pygame.font.init()
font = pygame.font.Font(None, 35)

lose1a = font.render('PLAYER 1 LOSE!', True,(255,0,0))
lose1b = font.render('PLAYER 1 LOSE!', True,(180,0,0))
lose2a = font.render('PLAYER 2 LOSE!', True,(255,0,0))
lose2b = font.render('PLAYER 2 LOSE!', True,(180,0,0))


Pscore1 = 0
Pscore2 = 0

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if self.rect.y < win_height - 100:
            self.rect.y += 1
        if keys[pygame.K_UP] and self.rect.y > -10:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_l(self):
        if self.rect.y < win_height - 100:
            self.rect.y += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > -10:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    

Pong1 = Player('rocketaL.png',0,180,80,150,4)
Pong2 = Player('rocketaR.png',520,180,80,150,4)
BallsInYoJaws = GameSprite('Balls.png',250,200,40,40,30)

dx = 3
dy = 3
ballspeed = -1
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))

        Pong1.update_l()
        Pong2.update_r()

        BallsInYoJaws.rect.x += dx
        BallsInYoJaws.rect.y += dy

        if pygame.sprite.collide_rect(Pong1,BallsInYoJaws) or pygame.sprite.collide_rect(Pong2,BallsInYoJaws):
            dx *= ballspeed
            ssound.play()
        if BallsInYoJaws.rect.y < 0 or BallsInYoJaws.rect.y > win_height-40:
            dy *= -1

        score_lA = font.render(str(Pscore1), True, (255,255,255))
        score_lB = font.render(str(Pscore1), True, (204,204,204))
        score_rA = font.render(str(Pscore2), True, (255,255,255))
        score_rB = font.render(str(Pscore2), True, (204,204,204))
        window.blit(score_lB,(32,12))
        window.blit(score_lA,(30,10))
        window.blit(score_rB,(win_width-43,12))
        window.blit(score_rA,(win_width-45,10))

        if BallsInYoJaws.rect.x < -50:
            msound.play()
            Pscore2 += 1
            BallsInYoJaws.rect.x = 280
            BallsInYoJaws.rect.x = 280
            ballspeed = -1

        if BallsInYoJaws.rect.x > win_width +10:
            msound.play()
            Pscore1 += 1
            BallsInYoJaws.rect.x = 280
            BallsInYoJaws.rect.x = 280
            ballspeed = -1

        if Pscore1 >= 3:
            finish = True
            window.blit(lose2b, (212, 222))
            window.blit(lose2a, (210, 220))
            BallsInYoJaws.rect.x = -50
            BallsInYoJaws.rect.y = -50

        if Pscore2 >= 3:
            finish = True
            window.blit(lose1b, (212, 222))
            window.blit(lose1a, (210, 220))
            BallsInYoJaws.rect.x = -50
            BallsInYoJaws.rect.y = -50
            
        Pong1.reset()
        Pong2.reset()
        BallsInYoJaws.reset()
    
    pygame.display.update()
    clock.tick(FPS)
