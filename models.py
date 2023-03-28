from pygame import *
FPS = 60

#coment
WINDOW_SIZE = (1000, 700)
SPRITE_SIZE = (10, 100)
BALL_SIZE = (50,50)
GREEN = (0, 255, 0)

window = display.set_mode(WINDOW_SIZE)
display.set_caption("Ping Pong")

font.init()
font_label = font.SysFont("Comic Sans MS", 32)

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, pos_x, pos_y, speed, size):
        super().__init__()
        self.image = transform.scale(image.load(image_name), size)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.size = size
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_pos(self, type):
        keys = key.get_pressed()
        if type == 1:
            if keys[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < WINDOW_SIZE[1] - SPRITE_SIZE[1]:
                self.rect.y += self.speed
        elif type == 2:
            if keys[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < WINDOW_SIZE[1] - SPRITE_SIZE[1]:
                self.rect.y += self.speed        