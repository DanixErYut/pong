import pygame import *
pygame.init()

#класс спрайта
class GameSprite(sprite.Sprite):
    def __init__(self,p_image,p_x,p_y,size_x,size_y,p_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(p_image),(size_x,size_y))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
#класс Игрока
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < 520:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.x < 520:
            self.rect.y += self.speed

window = display.set_mode((600,500))
window.fill((200,255,255))

game = True
clock = time.Clock()

while True:
    for e in event.get():
        if e.type ==QUIT:
            game = False
    display.update()
    clock.tick(60)
