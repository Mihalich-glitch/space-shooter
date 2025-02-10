import pygame 
from hero import MishaAugust

hero = MishaAugust

class Scores():
    def __init__(self, screen):
        self.image_hp = pygame.transform.scale(pygame.image.load('photo/health icon/heart icon.png').convert_alpha(), (30, 30))
        self.image_scores = pygame.transform.scale(pygame.image.load('photo/health icon/happy stars.png').convert_alpha(), (30, 30))
        self.screen = screen
        self.amount_stars = 0

    def show_health(self, hero):
        x = 30
        for hp in range(hero.health):
            self.screen.blit(self.image_hp, (x, 20))
            x += 30
    
    def draw_stars(self):
        print_score = pygame.font.SysFont('comicsansns', 50).render(str(self.amount_stars), True, (255, 255, 255))
        self.screen.blit(self.image_scores, (20, 70))
        self.screen.blit(print_score, (60, 70))