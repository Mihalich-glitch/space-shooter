import pygame
from bullet import Bullet

class MishaAugust:
    def __init__(self, screen):
        self.index = 0
        self.bullets = pygame.sprite.Group()  # Группа для хранения выпущенных пуль

        # Анимация движений
        self.move_right = [
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyright.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyright1.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyright2.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyright3.png').convert_alpha(), (50, 80))
        ]
        self.move_left = [
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyleft.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyleft1.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyleft2.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyleft3.png').convert_alpha(), (50, 80))
        ]
        self.move_up = [
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyup.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyup1.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyup2.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyup3.png').convert_alpha(), (50, 80))
        ]
        self.move_down = [
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboyoriginal.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboydown1.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboydown2.png').convert_alpha(), (50, 80)),
            pygame.transform.scale(pygame.image.load('photo/hero/pinkboydown3.png').convert_alpha(), (50, 80))
        ]
        #Изображение пистолета 
        self.pistol_image = pygame.transform.scale(pygame.image.load('photo/weapon/Guitar boss.png').convert_alpha(), (40, 40))
        
        self.pistol_mirror = pygame.transform.scale(pygame.image.load('photo/weapon/Guitar boss 2.png').convert_alpha(), (40, 40))
        self.pistol_image_right = self.pistol_mirror
        self.pistol_image_left = pygame.transform.flip(self.pistol_mirror, True, False)  # Зеркальное отражение

        self.screen = screen
        self.image = self.move_down[self.index]
        self.rect = self.image.get_rect(center=(450, 275))
        self.speed = 3
        self.health = 5

    def shoot(self, direction):
        # Создаем новую пулю и добавляем её в группу
        bullet = Bullet(self.rect.center, direction)
        self.bullets.add(bullet)

    def update(self, enemies, screen, scores):
        for bullet in self.bullets.sprites():
            self.screen.blit(bullet.image, bullet.rect)
            self.image = self.move_right[self.index // 4]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x < 1150:
            self.image = self.move_right[self.index // 4]
            self.rect.x += self.speed
            screen.blit(self.pistol_image, (self.rect.x + 25, self.rect.y + 32))
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.image = self.move_left[self.index // 4]
            self.rect.x -= self.speed
            screen.blit(self.pistol_image, (self.rect.x + 2, self.rect.y - 2))
        elif keys[pygame.K_UP] and self.rect.y > 0:
            self.image = self.move_up[self.index // 4]
            self.rect.y -= self.speed
            screen.blit(self.pistol_image, (self.rect.x + 5, self.rect.y - 0))
        elif keys[pygame.K_DOWN] and self.rect.y < 750:
            self.image = self.move_down[self.index // 4]
            self.rect.y += self.speed
            screen.blit(self.pistol_image, (self.rect.x - 0, self.rect.y + 41))

        if self.index < 11:
            self.index += 1
        else:
            self.index = 0

        # Обновляем состояние всех выпущенных пуль
        self.bullets.update()

        # Проверяем столкновения пуль с врагами
        hit_enemies = pygame.sprite.groupcollide(self.bullets, enemies, True, True)
        for _ in hit_enemies.values():  # За каждое попадание увеличиваем счетчик звезд
            scores.amount_stars += 1
        for bullet in hit_enemies:
            bullet.kill()

        # Отрисовываем все пули
        for bullet in self.bullets.sprites():
            screen.blit(bullet.image, bullet.rect)

        self.screen.blit(self.image, self.rect)
        
    def update_without_enemies(self):
        self.image = self.move_down[self.index // 4]
        if self.index < 11:
            self.index += 1
        else:
            self.index = 0
            
        self.screen.blit(self.image, self.rect)