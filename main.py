import pygame
import keyboard

from pysticks import *



pygame.init()

color = (123, 123, 123)

con = get_controller()

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