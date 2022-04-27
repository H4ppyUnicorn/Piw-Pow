from pygame import *
back = (0,0,0)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 90

font.init()
font = font.Font(None, 35)

lose1 = font.render('PLAYER 1 LOSE!', True,(180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True,(180,0,0))

Pscore1 = 0
Pscore2 = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    

Pong1 = Player('recta.png',0,120,20,150,5)
Pong2 = Player('recta.png',580,120,20,150,5)
BallsInYoJaws = GameSprite('Balls.png',250,200,40,40,16)

dx = 3
dy = 3
ballspeed = -1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)

        Pong1.update_l()
        Pong2.update_r()

        BallsInYoJaws.rect.x += dx
        BallsInYoJaws.rect.y += dy

        if sprite.collide_rect(Pong1,BallsInYoJaws) or sprite.collide_rect(Pong2,BallsInYoJaws):
            dx *= ballspeed
        if BallsInYoJaws.rect.y < 0 or BallsInYoJaws.rect.y > win_height-40:
            dy *= -1

        score_l = font.render(str(Pscore1), True, (255,255,255))
        score_r = font.render(str(Pscore2), True, (255,255,255))
        window.blit(score_l,(30,10))
        window.blit(score_r,(win_width-45,10))

        if BallsInYoJaws.rect.x < -50:
            Pscore2 += 1
            BallsInYoJaws.rect.x = 280
            BallsInYoJaws.rect.x = 280
            ballspeed = -1

        if BallsInYoJaws.rect.x > win_width +10:
            Pscore1 += 1
            BallsInYoJaws.rect.x = 280
            BallsInYoJaws.rect.x = 280
            ballspeed = -1

        Pong1.reset()
        Pong2.reset()
        BallsInYoJaws.reset()
    
    display.update()
    clock.tick(FPS)
