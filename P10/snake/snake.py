import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1080, 2180
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 48)

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

snake = [(100, 100), (80, 100), (60, 100)]

# RIGHT -> DOWN -> LEFT -> UP
directions = [(CELL, 0), (0, CELL), (-CELL, 0), (0, -CELL)]
dir_index = 0
direction = directions[dir_index]

score = 0
level = 1
foods_eaten = 0
speed = 8

# swipe tracking
swipe_start = None


def random_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:
            return (x, y)


food = random_food()


def draw():
    screen.fill(BLACK)

    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s, CELL, CELL))

    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()


def game_over():
    screen.fill(BLACK)
    msg = font.render("GAME OVER", True, RED)
    screen.blit(msg, (WIDTH // 2 - 160, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # swipe
        if event.type == pygame.MOUSEBUTTONDOWN:
            swipe_start = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP and swipe_start:
            swipe_end = pygame.mouse.get_pos()
            dx = swipe_end[0] - swipe_start[0]
            dy = swipe_end[1] - swipe_start[1]

            swipe_start = None

            # direction of swipe
            if abs(dx) > abs(dy) and abs(dx) > 20:
                if dx > 0:
                    # ->
                    dir_index = (dir_index + 1) % 4
                else:
                    # <-
                    dir_index = (dir_index - 1) % 4

                direction = directions[dir_index]

    # movement
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # death on walls
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        game_over()

    # death on tail
    if new_head in snake:
        game_over()

    snake.insert(0, new_head)

    # am am am
    if new_head == food:
        score += 1
        foods_eaten += 1
        food = random_food()

        if foods_eaten % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    draw()
    clock.tick(speed)