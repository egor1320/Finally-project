import pygame
import sys
from pygame import draw
from pygame.locals import *
import random

RED = (255, 0, 0)
GRAY = (150, 150, 150)
x = 535
y = 500

width, height = 1200, 800

spawn_timer = 0
fall_speed = 5
obj_list = []

def main():
    global x, y
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption(title="Game")

    # rect = Rect(600, 400, 20, 20)
    backgroung_image = pygame.image.load("depositphotos_556987214-stock-illustration-nature-scene-many-trees-hills.jpg").convert_alpha()
    backgroung_image = pygame.transform.scale(backgroung_image, (1200, 800))
    
    player_image = pygame.image.load("pngtree-an-empty-woven-wicker-basket-with-a-handle-used-for-storing-png-image_14588168.png").convert_alpha()
    player_image = pygame.transform.scale(player_image, (150, 150))
    
    score_image = pygame.image.load("pngtree-red-diamond-gemstone-clipart-illustration-png-image_13896903.png").convert_alpha()
    score_image = pygame.transform.scale(score_image,(50,50))

    # score_text = pygame.transform.scale(score_text, (100,50))

    while True:
        score = 0
        font = pygame.font.Font(None, 50)
        score_text = font.render(f"Счёт:{score}", True, (0,0,0))

        HP = 3
        font = pygame.font.Font(None, 50)
        HP_text = font.render(f"Жизни:{HP}", True, (0,0,0))

        for i in range:
            x_pos = random.randint(0)

        screen.blit(backgroung_image, (0, 0))
        screen.blit(HP_text,(1045,60))
        screen.blit(score_text,(1050,20))
        screen.blit(player_image, (x, y))
        # screen.blit(score_image,(x,y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= 2
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += 2
        elif keys[K_ESCAPE]:
            break

        if x >1065:
            x = 1065
        if x <-15:
            x = -15

        pygame.event.pump()
        pygame.display.flip()

if __name__ == "__main__":
    main()
