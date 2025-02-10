import pygame
# import backgroundanimation as bga
from random import randint , choice
from constants import WIDTH

enemyphoto = [
    pygame.transform.scale(pygame.image.load('photo/enemy/gold note.png'), (25,25)),
    pygame.transform.scale(pygame.image.load('photo/enemy/blue note.png'), (30,30)),
    pygame.transform.scale(pygame.image.load('photo/enemy/note1.png'), (35,35)),
    pygame.transform.scale(pygame.image.load('photo/enemy/deep blue note.png'), (35,35)),
    pygame.transform.scale(pygame.image.load('photo/enemy/magic note.png'), (35,35)),
    pygame.transform.scale(pygame.image.load('photo/enemy/pink note.png'), (35,35)),
]
class Antagonist(pygame.sprite.Sprite):
    def __init__(self,speed):
        super().__init__()
        self.image = choice(enemyphoto)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = WIDTH
        self.rect.y = randint(10, 750)
        

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)



        
        
