import pygame

"""ЗВУК НА ЗАДНЕМ ФОНЕ"""
def bg_music():
    pygame.mixer.init(44100, -16,2,2048)
    pygame.mixer.music.load('sound/thelema.mp3')
    pygame.mixer.music.play(-1)

"""ЗВУК ПРИ СТОЛКНОВЕНИИ С ПРОТИВНИКОМ"""
def sound_note():
    pygame.mixer.init(44100, -16,2,2048)
    sound_note = pygame.mixer.Sound('sound/re.mp3')
    sound_note.play()   