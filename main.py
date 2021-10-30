import pygame
import keyboard

#import pystick libary
from pysticks import *

#define con
con = get_controller()

#Initiate PyGame
pygame.init()

#defining
color1 = ('blue')
color2 = ('purple')
color3 = ('red')
color4 = ('orange')
colortxt = ('gray')

text = (0, 0, 0)

#Main Loop
while True:

    throttle = float("%+2.2f" % con.getThrottle())
    yaw = float("%+2.2f" % con.getYaw())
    pitch = float("%+2.2f" % con.getPitch())
    roll = float("%+2.2f" % con.getRoll())


    surface = pygame.display.set_mode((800, 600))


    #Yaw
    if yaw < 0:
        yaw = yaw + yaw * -2

        #draw the rectangles with dyamic sizes w1, h1, w2, h2
    pygame.draw.rect(surface, color1, pygame.Rect(100, 225, 600 * yaw, 50))
    pygame.draw.rect(surface, colortxt, pygame.Rect(110, 225, 175, 150))

    #Thorttle
    #draw the rectangles with dyamic sizes w1, h1, w2, h2
    pygame.draw.rect(surface, color2, pygame.Rect(100, 125, 600 * throttle, 50))
    pygame.draw.rect(surface, colortxt, pygame.Rect(100, 125, 175, 150))

    #Roll
    if roll < 0:
        roll = roll + roll * -2

    pygame.draw.rect(surface, color3, pygame.Rect(100, 325, 600 * roll, 50))
    pygame.draw.rect(surface, colortxt, pygame.Rect(100, 325, 175, 150))

    #Pitch
    if pitch < 0:
        pitch = pitch + pitch * -2

    #draw the rectangles with dyamic sizes w1, h1, w2, h2
    pygame.draw.rect(surface, color4, pygame.Rect(100, 425, 600 * pitch, 50))
    pygame.draw.rect(surface, colortxt, pygame.Rect(100, 425, 175, 150))
    pygame.display.flip()

    if keyboard.is_pressed('ctrl+q'):
            pygame.display.quit()
            print('Bye :)')
            break

    try:

            con.update()

            print('Throttle: %+2.2f   Roll: %+2.2f   Pitch: %+2.2f   Yaw: %+2.2f' %
                (con.getThrottle(), con.getRoll(), con.getPitch(), con.getYaw()))

    except KeyboardInterrupt:

        break


