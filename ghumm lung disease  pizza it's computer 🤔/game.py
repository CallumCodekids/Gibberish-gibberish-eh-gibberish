import pygame
import random
from move import move

screen = pygame.display.set_mode((1100, 573))

five_star_baby = pygame.image.load("5starbaby.jpg")
five_star_baby = pygame.transform.scale(five_star_baby,(screen.get_width(),
                                                        screen.get_height()))
mr_dragonsaur = pygame.image.load('pokemon.png')
dragonsaur_width = 60
dragonsaur_height = 200
mr_dragonsaur = pygame.transform.scale(mr_dragonsaur,(dragonsaur_width,
                                                      dragonsaur_height))
dragonsaur_x = screen.get_width()/2 - dragonsaur_width/2
dragonsaur_y = screen.get_height()/2 - dragonsaur_height/2
dragonsaur_speed = 1

the_shoe = pygame.image.load('please_not_the_shoe_nononononon.png')
the_shoe_width = 100
the_shoe_height = 500
the_shoe = pygame.transform.scale(the_shoe,(the_shoe_width,the_shoe_height))
the_shoe_poss = []
fps = 60
shoe_spawn_rate = 1
shoe_spawn_timer = 0
the_shoe_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
             running = False
    screen.blit(five_star_baby,(0,0))
    shoe_spawn_timer = shoe_spawn_timer + 1
    if shoe_spawn_timer > shoe_spawn_rate * fps:
        the_shoe_poss.append([random.randint(0, screen.get_width()-the_shoe_width), -the_shoe_height])
        shoe_spawn_timer = 0
    dragonsaur_x, dragonsaur_y = move(dragonsaur_x,
                                      dragonsaur_y,
                                      dragonsaur_width,
                                      dragonsaur_height,
                                      dragonsaur_speed,
                                      screen)
    screen.blit(mr_dragonsaur,(dragonsaur_x,dragonsaur_y))
    dragonsaur_rect = pygame.Rect(dragonsaur_x,dragonsaur_y, dragonsaur_width, dragonsaur_height)
    for pos in the_shoe_poss:
        pos[1] = pos[1] + the_shoe_speed
        screen.blit(the_shoe,(pos[0],pos[1]))
        shoe_rect = pygame.Rect(pos[0],pos[1], the_shoe_width, the_shoe_height)
        if dragonsaur_rect.colliderect(shoe_rect):
            running = False
        
        
    pygame.display.flip()
    clock.tick(fps)
    
print("I got squished :(")
print("I survived", len(the_shoe_poss),"shoes first though")
pygame.quit()