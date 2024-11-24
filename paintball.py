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
        self.player_image = transform.scale(image.load(player_image),(20,80))
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
font = font.SysFont("Arial", 20)
win_R = font.render(
    'Right player win', True, (0,0,0)
)
win_L = font.render(
    'Left player win', True, (0,0,0)
)

global timer
GAMEOVER = font.render(
    'Lose', True, (0,0,0)
)

restart = font.render(
    'want is restart game? Press Q', True, (255,255,255)
)

#--------------------------------------------------

score_L = 0
score_R = 0


#--------------------------------------------------
#
Player_1 = Player('platform.png', 20, 250, 5)
Player_2 = Player('platform.png', 650, 250, 5)
#Enemy
ball = Ball('painball_ball.png', 350, 250, 3,3)
#--------------------------------------------------
tick = 0
timer = 0
one = -1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        keys_pressed = key.get_pressed()
        if keys_pressed[K_q] and finish:
            ball.rect.x = 350
            ball.rect.y = 250
            Player_1.rect.y = 250
            Player_2.rect.y = 250
            score_L = 0
            score_R = 0
            finish = False
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
            ball.player_speed_x *= one
            ball.player_speed_y *= one
        if sprite.collide_rect(Player_2, ball):
            ball.player_speed_x *= one
            ball.player_speed_y *= one
        if ball.rect.x >= 650:
            ball.player_speed_x *= one
            score_R += 1
            ball.player_speed_x += 2
            ball.player_speed_y += 2
        if ball.rect.x <= 0:
            ball.player_speed_x *= one
            score_L += 1
            ball.player_speed_x += 2
            ball.player_speed_y += 2
        if ball.rect.y >= 420:
            ball.player_speed_y *= one
        if ball.rect.y <= 0:
            ball.player_speed_y *= one
    
        TIMERS = font.render('Время:' + str(timer), True, (255,255,255)) 
        window.blit(TIMERS,(250,20))
        Total_score_R = font.render('Очков у левого:' + str(score_R), True, (255,255,255)) 
        window.blit(Total_score_R,(20,20))
        Total_score_L = font.render('Очков у правого:' + str(score_L), True, (255,255,255)) 
        window.blit(Total_score_L,(500,20))
        
        if score_L == 10:
            finish = True
            window.blit(win_R,(350,250))
        if score_R == 10:
            finish = True
            window.blit(win_L,(350,250))

    if finish == True:
        window.blit(restart,(250,150))
        

        
        

    if tick == 60:
        timer += 1
        tick = 0
    tick += 1
    display.update()
    clock.tick(60)
#--------------------------------------------------
