import pygame
import sys
import random

pygame.init()

# Set up display
width = 640
height = 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake attributes
snake_size = 20
snake_speed = 8

# Font
font = pygame.font.SysFont(None, 40)


def message(text, color):
    msg = font.render(text, True, color)
    display.blit(msg, [width / 2, height / 2])


def game_loop():
    game_over = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
    food_y = round(random.randrange(0, height - snake_size) / snake_size) * snake_size

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        x += x_change
        y += y_change
        display.fill(white)
        pygame.draw.rect(display, green, [food_x, food_y, snake_size, snake_size])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Draw the snake
        for segment in snake_list:
            pygame.draw.rect(
                display, red, [segment[0], segment[1], snake_size, snake_size]
            )

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = (
                round(random.randrange(0, width - snake_size) / snake_size) * snake_size
            )
            food_y = (
                round(random.randrange(0, height - snake_size) / snake_size)
                * snake_size
            )
            length_of_snake += 1

        pygame.display.update()
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
