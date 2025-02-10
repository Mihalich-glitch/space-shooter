import pygame

from antagonist import Antagonist
from random import randint , choice
from boost import Boost
from restartmenu import restart
from game import *
# from sound import sound_note

def make_notaes(enemis, screen):
    enemis.update()
    enemis.draw(screen)
    if len(enemis) < 10:
        enemy = Antagonist(randint(1,4))
        enemis.add(enemy)
    

def make_boost(boost, screen):
    boost.update()
    boost.draw(screen)
    if len(boost) < 1:
        boostes = Boost(randint(1,6))
        boost.add(boostes)


def collide(hero, enemis):
    if pygame.sprite.spritecollide(hero, enemis, True):
        # sound_note()
        hero.health -= 1
    # if hero.health < 1:
    #     restart()

def collide_boost(hero, boost):
    effect = randint(1,5)
    if pygame.sprite.spritecollide(hero, boost, True):
        if effect == 1 or effect == 2:
            hero.health -= 2
            effect = randint(1,5)
        elif effect == 3 or effect == 4 or effect == 5: 
            hero.health += 1
            effect = randint(1,5)