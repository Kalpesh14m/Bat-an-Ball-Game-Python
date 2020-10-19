#BAT AND BALL

import pygame
from pygame.locals import *

pygame.init()

#set the height and width of the screen
size = [400,400]
screen = pygame.display.set_mode(size)

#setting the title for the screen
pygame.display.set_caption("Bat and Ball")

#This makes the normal mouse pointer invisible in graphical window
pygame.mouse.set_visible(0)

#creating a surface for the bat and the ball
bat_surf = pygame.Surface((64,12))
bat_surf.fill((136,89,55))
batrect = bat_surf.get_rect();

ball_surf = pygame.Surface((30,30))
ball_surf.fill((31,137,224),rect=None,special_flags=0)
ballrect = ball_surf.get_rect()

ball = pygame.draw.circle(ball_surf,(171,20,159),[16,16],15)

#set the speed of the ball
speed = [3,3]

#puts the bat center of the screen near the bottom
batrect.center = ((size[0]/2),(size[1] - 50))

#make a text object to display Game Over Message
font = pygame.font.Font(None,36)
text = font.render("Game Over",True,(255,0,0))
textRect = text.get_rect()
textRect.centerx = (size[0]/2)
textRect.centery = (size[1]/2)

#make a text object to display score
sfont = pygame.font.Font(None,16)
stext = sfont.render("",True,(255,255,255))
stextRect = stext.get_rect();
stextRect.centerx = (size[0]-70)
stextRect.centery = (10)


#loop until users clicks the close button
done = 0

#create a timer to update how often the screen updates
clock = pygame.time.Clock()

score = 0
#main game loop
while done == 0:
    screen.fill((31,137,224))
    
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=1
        #if not event.type == pygame.MOUSEMOTION:
        #    #move the ball
        #    ballrect.left += speed[0]
        #    ballrect.top  += speed[1]
            
        #move bat according to the mouse position
    position = pygame.mouse.get_pos()
    batrect.centerx = position[0]

    # move the ball
    ballrect.left += speed[0]
    ballrect.top  += speed[1]

    #collision detection
    if ballrect.colliderect(batrect):
        score += 1
        speed[1] = -speed[1]

    #check if the ball is going off-screen
    if ballrect.left < 0 or ballrect.right > size[0]:
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    #print "Game Over" if the ball leaves the screen
    if ballrect.top > size[1]:
        screen.blit(text,textRect)
        score = 0
        pygame.display.flip()
        pygame.time.wait(2000) #2000 milliseconds pause
        ballrect.top=0; ballrect.left=(size[0]/2) #reset the ball position        

    stext = sfont.render("Score : "+str(score),True,(255,255,255))
    screen.blit(stext,stextRect)
    screen.blit(ball_surf,ballrect)
    screen.blit(bat_surf,batrect)

    #set the loop to 60 cycles per second
    clock.tick(60)

    #update the display
    pygame.display.update()
        


        
            






