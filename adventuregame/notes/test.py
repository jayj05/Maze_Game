import pygame
import random
import sys 

class CrossHair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()  # Draw a rectangle around image

    def shoot(self):
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()



class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture_path), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)


clock = pygame.time.Clock()

WIDTH, HEIGHT = 900, 500 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.transform.scale(pygame.image.load("images/BG.png"), (WIDTH, HEIGHT))
pygame.mouse.set_visible(False)

crosshair = CrossHair("images/crosshair.png")  # Sprites cannot be drawn individually you have to draw them in a group
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("images/target.png", random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    target_group.add(new_target)

running = True 
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

    WIN.blit(background, (0, 0))
    target_group.draw(WIN)
    crosshair_group.draw(WIN)
    crosshair_group.update()
    pygame.display.update()
    

