import pygame 
from constants import WIDTH, HEIGHT, BACKGROUND

pygame.font.init()

def Nextlevel():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.transform.scale(pygame.image.load(BACKGROUND).convert(), (WIDTH, HEIGHT))