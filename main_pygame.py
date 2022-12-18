import pygame
import os

WHITE = 255, 255, 255
WIDTH, HEIGHT = 900, 500
CENTER = WIDTH / 2, HEIGHT / 2
FPS = 60
SHIPS_SCALE = 25, 15

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, SHIPS_SCALE), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, SHIPS_SCALE), 270)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot 'Em App")


def draw_window():
    win.fill(WHITE)
    win.blit(YELLOW_SPACESHIP_IMAGE, CENTER)
    win.blit(RED_SPACESHIP_IMAGE, (0, 0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    draw_window()


if __name__ == '__main__':
    main()
