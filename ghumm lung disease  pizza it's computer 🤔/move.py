import pygame


def move(x, y, width, height, speed, screen):
    og_x = x
    og_y = y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y = y - speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y = y + speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x = x - speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x = x + speed
    dragonsaur_rect = pygame.Rect(x,y, width, height)
    if not screen.get_rect().contains(dragonsaur_rect):
        return og_x, og_y

    return x,y
        
        