# Basic Initialization of pygame
import pygame
import random
import time

pygame.init()

from pygame.locals import (K_UP,K_a,K_s,K_d,K_w,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT)

# Set the screen
screen_height=600
screen_width=800
screen=pygame.display.set_mode([screen_width,screen_height])
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)

            # Keep player on the screen
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rect.right > screen_width:
                self.rect.right = screen_width
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= screen_height:
                self.rect.bottom = screen_height


# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()



#Add New Enemy

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)



player=Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)



runing=True

clock=pygame.time.Clock()

while runing:

    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                runing=False
        elif event.type==QUIT:
            runing=False


        elif event.type == ADDENEMY:

            new_enemy = Enemy()

            enemies.add(new_enemy)
            print("WE are inside an event")
            all_sprites.add(new_enemy)


    screen.fill((0, 0, 0))



    pressed_keys=pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()
        runing=False

    clock.tick(30)

    pygame.display.flip()



#Time to quite
pygame.quit()
