import pygame
from pygame.locals import *

screen_width , screen_height = 500, 500
img_path  = '/home/edutilos/Pictures/drozy.png'
start_x , start_y = 0 , 0
speed = 0.1

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pokemon = pygame.image.load(img_path)

position = (start_x, start_y)

clock.tick(40)

while True:
    # screen.fill(Color.BLACK)
    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            #pass
            continue
            # if event.key == pyK_ESCAPE:
            #     exit(0)

    position = (position[0] + speed, position[1])
    screen.blit(pokemon, position)
    pygame.display.flip()
    if position[0] > screen_width or position[0] < start_x:
        pokemon = pygame.transform.flip(pokemon, True, False)
        speed = -1 * speed
