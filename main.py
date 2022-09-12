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

# Game initialization
logging.basicConfig(filename="log.txt", level=logging.DEBUG)
logging.debug("App start up: " + str(today_time))

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Application")

# Main loop
while isRunning:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            isRunning = False

print("Ending the game")
time.sleep(0.5)
pygame.quit()
