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
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    display.update()
    clock.tick(FPS)