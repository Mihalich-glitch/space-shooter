import pygame
from constants import WIDTH, HEIGHT, CLOUDS

class Cloud():
    def __init__(self, iterator):
        self.iterator = iterator + 1
        
        self.image = pygame.transform.scale(pygame.image.load(CLOUDS[iterator]),(WIDTH, HEIGHT)).convert_alpha()
        self.rect = self.image.get_rect()
        self.moving_speed = 1.5
        self.bgaX1 = 0
        self.bgaY1 = 0
        self.bgaX2 = self.rect.width
        self.bgaY2 = 0


    def update(self):
        if self.iterator % 2 != 0:
            self.bgaX1 += self.moving_speed
            self.bgaX2 += self.moving_speed

            if self.bgaX1 >= self.rect.width:
                self.bgaX1 = - self.rect.width
            if self.bgaX2 >=  self.rect.width:
                self.bgaX2 = - self.rect.width
        else:
            self.bgaX1 -= self.moving_speed
            self.bgaX2 -= self.moving_speed

            if self.bgaX1 <= - self.rect.width:
                self.bgaX1 =  self.rect.width
            if self.bgaX2 <= - self.rect.width:
                self.bgaX2 =  self.rect.width
            
    
    def render(self, screen):
        screen.blit(self.image, (self.bgaX1, self.bgaY1))
        screen.blit(self.image, (self.bgaX2, self.bgaY2))

# class cloudyanimation2():
#     def __init__(self):
#         self.image = pygame.transform.scale(pygame.image.load(CLOUDS[1]),(WIDTH, HEIGHT))
#         self.rect = self.image.get_rect()
#         self.moving_speed = 1.5
#         self.bgaX1 = 0
#         self.bgaY1 = 0
#         self.bgaX2 = self.rect.width
#         self.bgaY2 = 0


#     def update(self):
#         self.bgaX1 -= self.moving_speed
#         self.bgaX2 -= self.moving_speed

#         if self.bgaX1 <= - self.rect.width:
#             self.bgaX1 =  self.rect.width
#         if self.bgaX2 <= - self.rect.width:
#             self.bgaX2 =  self.rect.width
            
    
#     def render(self, screen):
#         self.image.convert_alpha()
#         screen.blit(self.image, (self.bgaX1,self.bgaY1))
#         screen.blit(self.image, (self.bgaX2,self.bgaY2))

# class cloudyanimation3():
#     def __init__(self):
#         self.image = pygame.transform.scale(pygame.image.load('photo/background/cloudy3.jpg'),(1280, height))
#         self.rect = self.image.get_rect()
#         self.moving_speed = 1.5
#         self.bgaX1 = 0
#         self.bgaY1 = 0
#         self.bgaX2 = self.rect.width
#         self.bgaY2 = 0


#     def update(self):
#         self.bgaX1 += self.moving_speed
#         self.bgaX2 += self.moving_speed

#         if self.bgaX1 >= self.rect.width:
#             self.bgaX1 = - self.rect.width
#         if self.bgaX2 >=  self.rect.width:
#             self.bgaX2 = - self.rect.width
            
    
#     def render(self, screen):
#         self.image.convert_alpha()
#         screen.blit(self.image, (self.bgaX1,self.bgaY1))
#         screen.blit(self.image, (self.bgaX2,self.bgaY2))