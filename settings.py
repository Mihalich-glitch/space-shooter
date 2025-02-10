import pygame
import sys
import backgroundanimation as bga
pygame.font.init()

def settingmenu():
    window = (800,600)
    screen = pygame.display.set_mode(window)
    background = bga.backanimation()
    clock = pygame.time.Clock()

    font_small = pygame.font.Font(None, 30)
    exit_surface = pygame.Surface((100,50))
    exit_text = font_small.render('Exit',True, (255,0,0))
    exit_rect = exit_text.get_rect(
        center=(exit_surface.get_width() /2, 
                exit_surface.get_height()/2))
    exitbutton_rect = pygame.Rect(325,400,150,100)
    
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if exitbutton_rect.collidepoint(event.pos):
                    exit()

        if exitbutton_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(exit_surface, (127,255,212), (1,1,148,148))
        else:
            pygame.draw.rect(exit_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(exit_surface, (100, 100, 100), (1, 1, 148, 48))
            pygame.draw.rect(exit_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(exit_surface, (0, 100, 0), (1, 48, 148, 10), 2)

        background.update()
        background.render(screen)
        exit_surface.blit(exit_text,exit_rect)
        screen.blit(exit_surface,(exitbutton_rect.x ,exitbutton_rect.y))
        
        pygame.display.update()