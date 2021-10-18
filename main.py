import pygame
import keyboard

from pysticks import *

con = get_controller()

throttle = con.getThrottle()
yaw = con.getYaw()
pitch = float("%+2.2f" % con.getPitch())
roll = con.getPitch

#Initiate PyGame
pygame.init()

color1 = ('blue')
color2 = ('purple')
color3 = ('red')
color4 = ('orange')

text = (0, 0, 0)

#Main Loop
while True:

    throttle = float("%+2.2f" % con.getThrottle())
    yaw = float("%+2.2f" % con.getYaw())
    pitch = float("%+2.2f" % con.getPitch())
    roll = float("%+2.2f" % con.getRoll())


    surface = pygame.display.set_mode((800, 600))

    if yaw < 0:
        yaw = yaw + yaw * -2

        #draw the rectangles with dyamic sizes w1, h1, w2, h2
    pygame.draw.rect(surface, color1, pygame.Rect(100, 225, 600 * yaw, 50))


    #draw the rectangles with dyamic sizes w1, h1, w2, h2
    pygame.draw.rect(surface, color2, pygame.Rect(100, 125, 600 * throttle, 50))

    if roll < 0:
        roll = roll + roll * -2

    pygame.draw.rect(surface, color3, pygame.Rect(100, 325, 600 * roll, 50))

    if pitch < 0:
        pitch = pitch + pitch * -2

    #draw the rectangles with dyamic sizes w1, h1, w2, h2
    pygame.draw.rect(surface, color4, pygame.Rect(100, 425, 600 * pitch, 50))
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


