import time
import random
import logging
from datetime import date
from datetime import datetime

import pygame

width = 600
height = 600
isRunning = True
today_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
today_day = date.today().strftime("%b-%d-%Y")

red = (255, 0, 0)
blue = (0, 0, 255)

distance = 10

test_img = pygame.image.load("img/buttonLong_beige.png")
test_img_rect = test_img.get_rect()
test_img_rect.topleft = (100, 0)

# pygame.mixer.music.load("music/bossTheme.mp3")
# pygame.mixer.music.play(-1, 0.0)
# pygame.time.delay(3000)
# pygame.mixer.music.stop()

# Game initialization
logging.basicConfig(filename="log.txt", level=logging.DEBUG)
logging.debug("App start up: " + str(today_time))

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Application")

screen.fill(blue)
pygame.draw.rect(screen, red, (50, 50, 100, 100))

# Main loop
while isRunning:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            isRunning = False

        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_DOWN:
                if test_img_rect.y < screen.get_height():
                    test_img_rect.y += distance
                else:
                    test_img_rect.y = 0
                    test_img_rect.x += 50

    screen.blit(test_img, test_img_rect)
    pygame.display.update()

print("Ending the game")
time.sleep(0.5)
pygame.quit()
