import pygame
# from backgroundanimation import width, height
from constants import WIDTH, HEIGHT

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction):
        super().__init__()
        # Загружаем изображение пули
        self.image = pygame.transform.scale(pygame.image.load('photo/weapon/weapon2.png').convert_alpha(),(20, 20))
        self.rect = self.image.get_rect(center=position)
        # Направление движения пули (вправо или влево)
        self.direction = direction
        self.speed = 8  # Скорость пули

    def update(self):
        # Двигаем пулю в зависимости от направления
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        else:
            self.rect.x += self.speed

        # Уничтожение пули, если она выходит за пределы экрана
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()