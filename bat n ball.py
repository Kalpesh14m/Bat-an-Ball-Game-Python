# BAT AND BALL

import pygame
from pygame.locals import *
pygame.init()

# set the width and height of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)

# give the window a title
pygame.display.set_caption("Bat and Ball")

# This makes the normal mouse pointer invisible in graphics window
pygame.mouse.set_visible(0)

# create surfaces for the bat and ball
bat_surf = pygame.Surface((64,12))
bat_surf.fill((205,104,57))
batrect = bat_surf.get_rect()
ball_surf = pygame.Surface((30,30))
ballrect = ball_surf.get_rect()

ball = pygame.draw.circle(ball_surf, (255,64,64),[15, 15], 15)

# set speed of ball
speed = [3, 3]

# puts the bat centre of screen, near the bottom
batrect.center = ((size[0]/2), (size[1] - 50))

# make a text object
font = pygame.font.Font(None, 36)
text = font.render("Game Over", True, (255,0,0))
textRect = text.get_rect()
textRect.centerx = (size[0]/2)
textRect.centery = (size[1]/2)

# loop until the user clicks the close button
done=0

# create a timer to control how often the screen updates
clock = pygame.time.Clock()

# main game loop
while done == 0:

    screen.fill((0,0,0))

    # event handling
    for event in pygame.event.get(): # if we click something ...
        if event.type == pygame.QUIT: # if we click close ...
            done=1 # this will cause the loop to finish.

    # moves bat in accordance with the mouse position
    position = pygame.mouse.get_pos()
    batrect.centerx = position[0]

    # move the ball
    ballrect.left += speed[0]
    ballrect.top += speed[1]

    # collision detection
    if ballrect.colliderect(batrect):
        speed[1] = -speed[1]

    # check if the ball is going off screen
    if ballrect.left < 0 or ballrect.right > size[0]:
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    # print "Game Over" if the ball leaves screen
    if ballrect.top > size[1]:
        screen.blit(text, textRect)
        pygame.display.flip()
        pygame.time.wait(2000) # 2000 milliseconds pause
        ballrect.top=0; ballrect.left=(size[0]/2) # reset the ball position

    screen.blit(ball_surf, ballrect)
    screen.blit(bat_surf, batrect)

    # set the loop to 60 cycles per second
    clock.tick(60)

    # update the display
    pygame.display.flip()
