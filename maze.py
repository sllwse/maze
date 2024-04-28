#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and y1 > 0:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and y1 < 400:
            self.rect.y += 10
        if keys_pressed[K_LEFT] and x1 > 0:
            self.rect.x -= 10
        if keys_pressed[K_RIGHT] and x1 < 600:
            self.rect.x += 10           

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 700 - 50:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
         window.blit(self.image, (self.rect.x, self.rect.y))



#создай окно игры
window = display.set_mode((700, 500))

#задай фон сцены
display.set_caption('сдохни или умри')

#создай 2 спрайта и размести их на сцене
background = transform.scale(image.load('background.jpg'), (700, 500))
hero = Player('hero.png', 20, 20, 10)
x1 = 100
y1 = 100
haggy = Enemy('haggy.png', 400, 280, 6)
x2 = 400
y2 = 280
wall = Wall(190, 91, 75, 100, 0, 10, 400)
wall_1 = Wall(190, 91, 75, 100, 400, 250, 10)
wall_2 = Wall(190, 91, 75, 180, 250, 150, 10)

font.init()
font = font.Font(None, 70)
lose = font.render("LOSER!!!", True, (123, 123, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
kick.play()

clock = time.Clock()
FPS = 60

#обработай событие «клик по кнопке "Закрыть окно"»
finish = False
game = True
while game:
    window.blit(background, (0,0))
    hero.update()
    hero.reset()
    haggy.update()
    haggy.reset() 
    wall.draw_wall()        
    wall_1.draw_wall()
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if finish != True:
        if sprite.collide_rect(hero, haggy):
            finish = False
            window.blit(lose, (123, 123))
            
            finish = True
        display.update()
        clock.tick(FPS)



