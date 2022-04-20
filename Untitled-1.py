from pygame import *
back = (0,0,0)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
background = transform.scale(image.load('doggo.jpg'), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 30

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
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    

Pong1 = Player('leftpong.png',0,120,100,300,15)
Pong2 = Player('rightpong.png',500,120,100,300,15)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)

        Pong1.update_l()
        Pong2.update_r()

        Pong1.reset()
        Pong2.reset()
    
    display.update()
    clock.tick(FPS)
