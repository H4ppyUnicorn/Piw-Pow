from pygame import *
back = (0,0,0)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

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
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 200:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 200:
            self.rect.y += self.speed
    

Pong1 = Player('recta.png',0,120,20,200,5)
Pong2 = Player('recta.png',580,120,20,200,5)
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
            dx *= ballspeed - 0.1
        if BallsInYoJaws.rect.y < 0 or BallsInYoJaws.rect.y > win_height-40:
            dy *= -1

        Pong1.reset()
        Pong2.reset()
        BallsInYoJaws.reset()
    
    display.update()
    clock.tick(FPS)
