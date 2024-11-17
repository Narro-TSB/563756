from pygame import *

#Class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.player_image = transform.scale(image.load(player_image),(65,65))
        self.rect = self.player_image.get_rect()
        self.player_speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = ''
    def reset(self):
        window.blit(self.player_image, (self.rect.x, self.rect.y))
#--------------------------------------------------
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.player_image = transform.scale(image.load(player_image),(10,65))
        self.rect = self.player_image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.player_speed
        if keys_pressed[K_s] and self.rect.y <= 435:
            self.rect.y += self.player_speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.player_speed
        if keys_pressed[K_DOWN] and self.rect.y <= 435:
            self.rect.y += self.player_speed
#--------------------------------------------------
class Ball(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y):
        super().__init__()
        self.player_image = transform.scale(image.load(player_image),(65,65))
        self.rect = self.player_image.get_rect()
        self.player_speed_x = player_speed_x
        self.player_speed_y = player_speed_y
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = ''
    def reset(self):
        window.blit(self.player_image, (self.rect.x, self.rect.y))
    def Gameover(self):
        global finish
        if self.rect.x >= 620:
            finish = False

        if self.rect.x <= 0:
            finish = False
            
    def update(self):
            self.rect.x += self.player_speed_x 
            self.rect.y += self.player_speed_y
#--------------------------------------------------
window = display.set_mode((700,500))
background = transform.scale(image.load("background.png"),(700,500))
window.blit(background,(0,0))
#--------------------------------------------------
clock = time.Clock()
#--------------------------------------------------
game = True
finish = False
#--------------------------------------------------
font.init()
font = font.SysFont("Arial", 40)
win = font.render(
    'YOU WIN!', True, (255,215,0)
)
global timer
GAMEOVER = font.render(
    'Lose', True, (160,0,0)
)
#--------------------------------------------------

score_L = 0
score_R = 0

#--------------------------------------------------
#Players
Player_1 = Player('platform.png', 20, 250, 5)
Player_2 = Player('platform.png', 650, 250, 5)
#Enemy
ball = Ball('painball_ball.png', 350, 250, 5,3)
#--------------------------------------------------
tick = 0
timer = 0
one = -1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        #Blit sprites
        Player_1.update()
        Player_2.update1()
        Player_1.reset()
        Player_2.reset()
        ball.update()
        ball.reset()

        if sprite.collide_rect(Player_1, ball):
            print('dffddf')
            ball.player_speed_x *= one
        if sprite.collide_rect(Player_2, ball):
            ball.player_speed_x *= one
        if ball.rect.x >= 650:
            ball.player_speed_x *= one
            finish = False
        if ball.rect.x <= 0:
            ball.player_speed_x *= one
            finish = False
        if ball.rect.y >= 420:
            ball.player_speed_y *= one
        if ball.rect.y <= 0:
            ball.player_speed_y *= one
    
    TIMERS = font.render('Время:' + str(timer), True, (255,215,0)) 
    window.blit(TIMERS,(350,50))

    if tick == 60:
        timer += 1
        tick = 0
    tick += 1
    display.update()
    clock.tick(60)
#--------------------------------------------------