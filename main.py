import pygame
import sys
from pygame import draw
from pygame.locals import *
import random

clock = pygame.time.Clock()

RED = (255, 0, 0)
GRAY = (150, 150, 150)
x = 535
y = 500
var = 0
max_var = 100
width, height = 1200, 800
spawn = 0
spawn_rate = 100
fall_speed = 2
obj_list = []
obj_positions = []
speed = 5

def spawn_item_chance() -> bool:
    return random.randint(1, spawn_rate) == 1

def main():
    global x, y, fall_speed, spawn_rate, speed

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

    while True:
        
        score = 0
        font = pygame.font.Font(None, 50)
        score_text = font.render(f"Счёт:{score}", True, (0,0,0))

        HP = 3
        font = pygame.font.Font(None, 50)
        HP_text = font.render(f"Жизни:{HP}", True, (0,0,0))

        screen.blit(backgroung_image, (0, 0))
        screen.blit(HP_text,(1045,60))
        screen.blit(score_text,(1050,20))
        screen.blit(player_image, (x, y))

        if spawn_item_chance():
            x2 = random.randint(0, 1200)
            rect = score_image
            obj_list.append({"rect": rect, "pos": {"x": x2, "y": -20}})
            spawn_rate = spawn_rate if spawn_rate == 2 else spawn_rate-1
            if (spawn_rate % 10 == 0): speed += 1
            # print("Spawn rate: ", spawn_rate)
            # print("Speed: ", speed)

        clock.tick(60)

        for rect in obj_list:
            screen.blit(rect["rect"], (rect["pos"]["x"], rect["pos"]["y"]))
            rect["pos"]["y"] = rect["pos"]["y"] if rect["pos"]["y"] == 790 else rect["pos"]["y"] + fall_speed
            
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += speed
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
