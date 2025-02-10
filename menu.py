"""ИМПОРТЫ"""
import pygame
import sys

"""ФРОМЫ РАЗДЕЛОВ МЕНЮ"""
from game import run    # Импорт запуска игры
from settings import settingmenu    # Импорт окна настроек

"""ОСТАЛЬНЫЕ ФРОМЫ"""
from constants import *
from hero import MishaAugust

pygame.font.init()
"""Переменные, храняшие в себе настройки экрана"""
screen = pygame.display.set_mode((WIDTH, HEIGHT))   # Экран
background = pygame.transform.scale(pygame.image.load(BACKGROUND).convert(), (WIDTH, HEIGHT))  # Загрузка изображения фона
font_small = pygame.font.Font('FONT/static/PixelifySans-Medium.ttf', 50)    # Шрифт

"""Создание поверхности для кнопки"""
play_surface = pygame.Surface((300, 150))
settings_surface = pygame.Surface((300, 150))
exit_surface = pygame.Surface((300, 150))

"""Отображение текста на кнопке"""
play_text = font_small.render('Play', True, STANDART_TEXT_COLOR)
settings_text = font_small.render('Settings', True, STANDART_TEXT_COLOR)
exit_text = font_small.render('Exit', True, STANDART_TEXT_COLOR)

play_rect = play_text.get_rect(
    center=(150, 
            75))
settings_rect = settings_text.get_rect(
    center=(settings_surface.get_width() / 2, 
            settings_surface.get_height() / 2))
exit_rect = exit_text.get_rect(
    center=(exit_surface.get_width() / 2, 
            exit_surface.get_height() / 2))

"""Границы кнопок"""
playbutton_rect = pygame.Rect(200, HEIGHT//2-200, 200, 90)
settingsbutton_rect = pygame.Rect(200, HEIGHT//2-100, 250, 90)
exitbutton_rect = pygame.Rect(200, HEIGHT//2, 200, 100)

"""Объявление и параметры игрока"""
player = MishaAugust(screen)
player.rect = player.image.get_rect(center=(800, -20))
player.speed = 1

"""Объявление стрелок"""
# arrow_up_surface = pygame.Surface((80, 90))
# arrow_down_surface = pygame.Surface((80, 90))

arrow_right_sufrace = pygame.transform.scale(pygame.image.load(RIGHT_ARROW).convert(), (45, 50))
arrow_left_sufrace = pygame.transform.scale(pygame.image.load(LEFT_ARROW).convert(), (45, 50))

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if playbutton_rect.collidepoint(event.pos):
                run()
            if settingsbutton_rect.collidepoint(event.pos):
                settingmenu()
            if exitbutton_rect.collidepoint(event.pos):
                exit()
    """Наведение игрока на кнопки"""
    if playbutton_rect.collidepoint(pygame.mouse.get_pos()):
        play_text = font_small.render('Play',True, (HOVER_TEXT_COLOR))
    elif settingsbutton_rect.collidepoint(pygame.mouse.get_pos()):
        settings_text = font_small.render('Settings', True, (HOVER_TEXT_COLOR))
    elif exitbutton_rect.collidepoint(pygame.mouse.get_pos()):
        exit_text = font_small.render('Exit', True, (HOVER_TEXT_COLOR))
    else:
        play_text = font_small.render('Play',True, (STANDART_TEXT_COLOR))
        settings_text = font_small.render('Settings', True, (STANDART_TEXT_COLOR))
        exit_text = font_small.render('Exit', True, STANDART_TEXT_COLOR)
    
    """Отображение текстов кнопок"""
    play_surface.blit(play_text, play_rect)
    settings_surface.blit(settings_text, settings_rect)
    exit_surface.blit(exit_text, exit_rect)

    """Обновление экрана"""
    screen.blit(background, (0, 0))
    
    """Отображение кнопок на экране"""
    screen.blit(play_surface,(playbutton_rect.x ,playbutton_rect.y))
    screen.blit(settings_surface,(settingsbutton_rect.x ,settingsbutton_rect.y))
    screen.blit(exit_surface,(exitbutton_rect.x ,exitbutton_rect.y))
    
    """Обновление игрока"""
    if player.rect.centery != HEIGHT//2:
        player.rect.centery += player.speed
    # if player.rect.centery == HEIGHT//2:
    
    if player.rect.centery == HEIGHT//2:
        screen.blit(arrow_right_sufrace, (player.rect.x + 60, player.rect.y + 10))
        screen.blit(arrow_left_sufrace, (player.rect.x - 55, player.rect.y + 10)) 
    
    player.update_without_enemies()
    

    
    """Обновление экрана"""
    clock.tick(FPS)
    pygame.display.update()
