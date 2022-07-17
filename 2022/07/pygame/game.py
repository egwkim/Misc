import pygame
import math
import sys
from pygame.locals import *

width = 600
height = 400
fps = 30

white = (255, 255, 255)
black = (0,   0,   0)
green = (0, 255,   0)

player_text = '🤔'


def main():
    global window, clock, emoji_font, text_font
    pygame.init()
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    emoji_font = pygame.font.SysFont('Segoe UI Emoji', 50)
    text_font = pygame.font.SysFont('Segoe UI', 50)
    pygame.display.set_caption('My First Pygame!')

    load_screen()
    play()
    game_over()
    pygame.quit()
    sys.exit()


def draw_rect_angle(surf, rect, pivot, angle, color):
    pts = [rect.topleft, rect.topright, rect.bottomright, rect.bottomleft]
    pts = [(pygame.math.Vector2(p) - pivot).rotate(-angle) + pivot for p in pts]
    pygame.draw.lines(surf, color, True, pts, 3)


def render_player(pos, angle=0, color=black):
    player = emoji_font.render(player_text, 1, color)
    player_rect_original = player.get_rect()
    player_rect_original.center = pos
    player = pygame.transform.rotate(player, angle)
    player_rect = player.get_rect()
    player_rect.center = pos

    window.blit(player, player_rect)
    draw_rect_angle(window, player_rect_original, pos, angle, green)


def load_screen():
    for i in range(0, 101, 10):
        window.fill(white)
        render_player((i, height / 2))
        pygame.display.update()
        clock.tick(fps)
    i = 0
    text = text_font.render(f'Press space to start!', 1, black)
    text_rect = text.get_rect()
    text_rect.center = (width/2, 90)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return
        window.fill(white)

        i += 1
        if i < 25:
            window.blit(text, text_rect)
        elif i == 50:
            i = 0

        render_player((100, height / 2))
        pygame.display.update()
        clock.tick(fps)


def play():
    border = emoji_font.render(player_text, 1, black).get_height() / 2
    max_y = height - border
    min_y = border

    x = 100
    y = height / 2
    vx = 10
    vy = 0

    moveUp = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    moveUp = True
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    moveUp = False

        if moveUp:
            vy += 1
        else:
            vy -= 1

        angle = math.degrees(math.atan(vy/vx))
        y -= vy

        if y > max_y:  # Collides on ceiling
            y = max_y
            if angle < 0:
                angle = 0
                vy = 0
        if y < min_y:  # Collides on floor
            y = min_y
            if angle > 0:
                angle = 0
                vy = 0

        if False:  # TODO Add game over condition
            return

        window.fill(white)
        render_player((x, y), angle)

        pygame.display.update()
        clock.tick(fps)


def game_over():
    pass


if __name__ == '__main__':
    main()
