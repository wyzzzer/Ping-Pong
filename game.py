from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(GameSprite):
    def moveLeftRacket(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500-100:
            self.rect.y += self.speed
    def moveRightRacket(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500-100:
            self.rect.y += self.speed

win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
window.fill((255, 255, 255))

r1 = Racket('racket.png', 30, 250, 20, 100, 5)
r2 = Racket('racket.png', 620, 250, 20, 100, 5)
ball = GameSprite('ball.png', 300, 200, 50, 50, 10)

font.init()
font = font.Font(None, 35)
loseLeft = font.render('LEFT PLAYER LOSE !', True, (180, 0, 0))
loseRight = font.render('RIGHT PLAYER LOSE !', True, (180, 0, 0))

game = True
run = True
clock = time.Clock()
ball_x = 3
ball_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if run == True:
        window.fill((255, 255, 255))
        r1.moveLeftRacket()
        r2.moveRightRacket()
        ball.rect.x += ball_x
        ball.rect.y += ball_y

        if sprite.collide_rect(r1, ball) or sprite.collide_rect(r2, ball): 
            ball_x *= -1

        if ball.rect.y > win_height or ball.rect.y < 0:
            ball_y *= -1

        if ball.rect.x < 0:
            run = False
            window.blit(loseLeft, (200, 200))

        if ball.rect.x > win_width:
            run = False
            window.blit(loseRight, (200, 200))
        r1.reset()
        r2.reset()
        ball.reset()

    display.update()
    clock.tick(60)