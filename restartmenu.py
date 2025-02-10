import pygame
import sys
from game import *
import backgroundanimation as bga

from constants import *

pygame.font.init()
def restart():
    """Переменные, хранящие в себе настройки экрана"""
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font_small = pygame.font.Font('FONT/static/PixelifySans-Medium.ttf', 50)
    """Background animation (под вопросом использования)"""
    background = bga.backanimation()

    """Создание поверхности для кнопок"""
    restart_surface = pygame.Surface((425, 50))
    exit_surface = pygame.Surface((308, 50))

    """Отображение текста на кнопке"""
    lose_text = font_small.render('DEFEAT',True, (STANDART_TEXT_COLOR)) # рисует наш текст и задаем ему цвет
    restart_text = font_small.render('Restart',True, (STANDART_TEXT_COLOR))
    exit_text = font_small.render('Exit',True, (STANDART_TEXT_COLOR))

    """Отображение текста на кнопке"""
    play_rect = restart_text.get_rect(
        center=(restart_surface.get_width() / 2 - 100, 
                restart_surface.get_height() / 2))
    exit_rect = exit_text.get_rect(
        center=(exit_surface.get_width() / 2 - 100, 
                exit_surface.get_height() / 2))

    """Границы кнопок"""
    lose_rect = pygame.Rect(325,200,400,350)
    playbutton_rect = pygame.Rect(325,300, 150, 100)
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
            restart_text = font_small.render('Restart', True, (HOVER_TEXT_COLOR))
        elif exitbutton_rect.collidepoint(pygame.mouse.get_pos()):
            exit_text = font_small.render('Exit', True, (HOVER_TEXT_COLOR))
        else:
            restart_text = font_small.render('Restart',True, (STANDART_TEXT_COLOR))
            exit_text = font_small.render('Exit',True, (STANDART_TEXT_COLOR))
        
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