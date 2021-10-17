import pygame
import keyboard

pygame.init()

color = (123, 123, 123)

while True:
    surface = pygame.display.set_mode((800, 600))

    if keyboard.is_pressed('ctrl+q'):
            pygame.display.quit()
            print('Bye :)')
            break