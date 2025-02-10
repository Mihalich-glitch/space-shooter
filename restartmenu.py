import pygame
import sys
from game import *
import backgroundanimation as bga

pygame.font.init()
def restart():
    window = (800,600)
    screen = pygame.display.set_mode(window)
    background = bga.backanimation()

    font_small = pygame.font.Font(None, 30)

    restart_surface = pygame.Surface((100,50)) # задает размер
    exit_surface = pygame.Surface((100,50))

    lose_text = font_small.render('You Lose!',True, (255,0,0)) # рисует наш текст и задаем ему цвет
    restart_text = font_small.render('Restart',True, (0,255,0))
    exit_text = font_small.render('Exit',True, (255,0,0))
    play_rect = restart_text.get_rect(
        center=(restart_surface.get_width() /2, 
                restart_surface.get_height()/2)) # прикрепляем наш текст к рачположению на экране
    exit_rect = exit_text.get_rect(
        center=(exit_surface.get_width() /2, 
                exit_surface.get_height()/2))

    lose_rect = pygame.Rect(325,200,400,350)
    playbutton_rect = pygame.Rect(325,300,150,100)
    exitbutton_rect = pygame.Rect(325,400,150,100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if playbutton_rect.collidepoint(event.pos):
                    pygame.quit()
                    run()
                if exitbutton_rect.collidepoint(event.pos):
                    pygame.quit()
                    return

        if playbutton_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(restart_surface, (127,255,212), (1,1,148,148))
        else:
            pygame.draw.rect(restart_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(restart_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(restart_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(restart_surface, (0, 100, 0), (1, 48, 148, 10), 2)

        if exitbutton_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(exit_surface, (127,255,212), (1,1,148,148))
        else:
            pygame.draw.rect(exit_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(exit_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(exit_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(exit_surface, (0, 100, 0), (1, 48, 148, 10), 2)
        
        background.update()
        background.render(screen)
        restart_surface.blit(restart_text,play_rect)
        exit_surface.blit(exit_text,exit_rect)

        screen.blit(lose_text,lose_rect)
        screen.blit(restart_surface,(playbutton_rect.x ,playbutton_rect.y))
        screen.blit(exit_surface,(exitbutton_rect.x ,exitbutton_rect.y))

        
        pygame.display.update()

if __name__ == "__main__":
    restart()