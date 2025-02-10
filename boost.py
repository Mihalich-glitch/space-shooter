import pygame 
from random import randint
from constants import WIDTH

class Boost(pygame.sprite.Sprite):
    def __init__(self,speed):
        self.index = 1
        super().__init__()

        self.boost_photo = [
    pygame.transform.scale(pygame.image.load('photo/boost/cocacolaright.png'), (50,50)),
    pygame.transform.scale(pygame.image.load('photo/boost/cocacolaleft.png'), (50,50)),   
]
        self.image = self.boost_photo[self.index]
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = WIDTH
        self.rect.y = randint(10, 750)
        

    def update(self):
        self.rect.x -= self.speed
        self.image = self.boost_photo[self.index // 2]
        if self.rect.x < 0:
            self.kill()
        
        if self.index < 3:
            self.index += 1
        else:
            self.index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
 