import pygame
import keyboard

from pysticks import *

con = get_controller()

throttle = con.getThrottle()
yaw = con.getYaw()
pitch = "Pitch: %+2.2f" % con.getPitch()
roll = con.getPitch

#Initiate PyGame
pygame.init()

color = (123, 123, 123)

#Main Loop
while True:
    surface = pygame.display.set_mode((800, 600))

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

    pygame.draw.rect(surface, color, pygame.Rect(float(100, 100, 150 + float(pit), 105)))
    pygame.display.flip()
