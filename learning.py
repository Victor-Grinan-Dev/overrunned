import pygame.mixer
from colors import *
import random

#  initiate pygame
pygame.init()
WIDTH, HEIGTH = 1270, 650

#  create screen
screen = pygame.display.set_mode((WIDTH, HEIGTH))

#  title and icon
pygame.display.set_caption("Razorback Overruned")
icon = pygame.image.load('images/0_hammer_icon.png')
pygame.display.set_icon(icon)

player_img = pygame.image.load('images/rhino.png')
PLAYER_SIZEX = 44
PLAYER_SIZEY = 64
playerX = WIDTH / 2 - PLAYER_SIZEX / 2
playerY = HEIGTH / 2 - PLAYER_SIZEY / 2
player_coor = (playerX, playerY)
player_speed = 1
directionY = 0
directionX = 0

# Initialing Color
color = (255, 0, 0)

clock = pygame.time.Clock()

enemy_list = []


#  player

def player():
    screen.blit(player_img, (playerX, playerY))


# enemy

enemy_img = pygame.image.load('images/circle.png')

enemyY = 10
enemy_speed = 1.5


def set_enemy_start_pos():
    return random.randint(10, 1200)


enemyX = set_enemy_start_pos()


def enemy():
    screen.blit(enemy_img, (enemyX, enemyY))


def enemy_move(x, y):
    # todo: move towards the player
    pass


def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)


while True:

    clock.tick(120)

    screen.fill(dark_green)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                directionY = -1
            if event.key == pygame.K_s:
                directionY = 1
            if event.key == pygame.K_a:
                directionX = -1
            if event.key == pygame.K_d:
                directionX = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                directionY = 0
            if event.key == pygame.K_s:
                directionY = 0
            if event.key == pygame.K_a:
                directionX = 0
            if event.key == pygame.K_d:
                directionX = 0
        #     playerY += player_speed

    player()
    enemy()

    enemy_move()

    playerY += directionY * player_speed
    playerX += directionX * player_speed
    if playerY < 0:
        playerY = 0
    elif playerY > HEIGTH - PLAYER_SIZEY:
        playerY = HEIGTH - PLAYER_SIZEY
    if playerX < 0:
        playerX = 0
    elif playerX > WIDTH - PLAYER_SIZEX:
        playerX = WIDTH - PLAYER_SIZEX

    pygame.display.update()
    pygame.display.flip()
