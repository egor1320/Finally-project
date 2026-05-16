import pygame
import sys
from pygame import draw
from pygame.locals import *


RED = (255, 0, 0)
GRAY = (150, 150, 150)

PLAYER_POSITION = (535, 500)

def key_pressed(key):
    match key:
        case pygame.K_LEFT:
            PLAYER_POSITION['x'] -= 10 
        case esc:
            return False
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption(title="Game")

    rect = Rect(600, 400, 20, 20)
    backgroung_image = pygame.image.load("depositphotos_556987214-stock-illustration-nature-scene-many-trees-hills.jpg").convert_alpha()
    backgroung_image = pygame.transform.scale(backgroung_image, (1200, 800))
    
    player_image = pygame.image.load("pngtree-an-empty-woven-wicker-basket-with-a-handle-used-for-storing-png-image_14588168.png").convert_alpha()
    player_image = pygame.transform.scale(player_image, (150, 150))
    
    screen.blit(backgroung_image, (0, 0))
    screen.blit(player_image, PLAYER_POSITION)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            PLAYER_POSITION -= (10, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            PLAYER_POSITION += (10, 0)
        
        pygame.event.pump()

        pygame.draw.rect(screen, RED, rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()
