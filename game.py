import pygame 
# import backgroundanimation as bga
from cloudy import Cloud
import events
from hero import MishaAugust
# from sound import bg_music
from scores import Scores
from pygame.locals import *

import backgroundanimation as bga   # ВРЕМЕННО

from constants import WIDTH, HEIGHT, CLOUDS, BACKGROUND

"""СЛУЖЕБНЫЕ ФУНКЦИИ"""
def get_shoot_direction():
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        return 'right'
    elif keys[K_LEFT]:
        return 'left'
    elif keys[K_UP]:
        return 'up'
    elif keys[K_DOWN]:
        return 'down'
    else:
        return None
clock = pygame.time.Clock()

"""ОСНОВНАЯ ПРОГРАММА"""
def run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.transform.scale(pygame.image.load(BACKGROUND).convert(), (WIDTH, HEIGHT))  # Загрузка изображения фона
    clouds = []
    for i in range(len(CLOUDS)):
        cloud = Cloud(i)
        clouds.append(cloud)
    hero = MishaAugust(screen)
    enemies = pygame.sprite.Group()
    boost = pygame.sprite.Group()
    scores = Scores(screen)

    bullets = pygame.sprite.Group()  # Группа для хранения выпущенных пуль

#  bg_music()
    while True:    
        clock.tick(90)   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    direction = get_shoot_direction() # Функция для определения направления стрельбы 
                    hero.shoot(direction)
            
        if hero.health < 1:
            restart()
        """ФУНКЦИИ ДЛЯ ОБНОВЛЕНИЯ КАРТИНОК НА ЭКРАНЕ"""
        screen.blit(background, (0, 0))
        
        for cloud in clouds:
            cloud.update()
            cloud.render(screen)

        hero.update(enemies, screen, scores)
        hero.bullets.update()
        hero.bullets.draw(screen) 
        scores.show_health(hero)
        scores.draw_stars() 
        events.make_notaes(enemies, screen)
        events.collide(hero , enemies)
        events.make_boost(boost,screen)
        events.collide_boost(hero, boost)
        enemies.update()
        enemies.draw(screen)
        boost.update()
        boost.draw(screen)
        
        pygame.display.flip()

"""ОКНО РЕСТАРТА"""
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
                return
                
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
    run()         