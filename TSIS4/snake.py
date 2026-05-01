import pygame
import random
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1080, 2180
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 48)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Food types: color, score value, spawn weight, lifetime (seconds)
FOOD_TYPES = [
    {"color": (255, 0, 0), "score": 1, "weight": 70, "lifetime": 14},   # common
    {"color": (0, 0, 255), "score": 3, "weight": 20, "lifetime": 10},    # rare
    {"color": (255, 255, 0), "score": 5, "weight": 10, "lifetime": 7},  # very rare
]

snake = [(100, 100), (80, 100), (60, 100)]

# RIGHT -> DOWN -> LEFT -> UP
directions = [(CELL, 0), (0, CELL), (-CELL, 0), (0, -CELL)]
dir_index = 0
direction = directions[dir_index]

score = 0
level = 1
foods_eaten = 0
speed = 8

swipe_start = None


def weighted_food_choice():
    """Choose food type based on weight (probability)."""
    weights = [f["weight"] for f in FOOD_TYPES]
    return random.choices(FOOD_TYPES, weights=weights, k=1)[0]


def spawn_food():
    """Spawn food at random position with random type and timer."""
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:
            food_type = weighted_food_choice()
            return {
                "pos": (x, y),
                "type": food_type,
                "spawn_time": time.time()
            }


food = spawn_food()


def draw():
    screen.fill(BLACK)

    # Draw snake
    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s, CELL, CELL))

    # Draw food
    pygame.draw.rect(screen, food["type"]["color"], (*food["pos"], CELL, CELL))

    # Draw UI text
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()


def game_over():
    """Display game over screen."""
    screen.fill(BLACK)
    msg = font.render("GAME OVER", True, (255, 0, 0))
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

        # Swipe start
        if event.type == pygame.MOUSEBUTTONDOWN:
            swipe_start = pygame.mouse.get_pos()

        # Swipe end
        if event.type == pygame.MOUSEBUTTONUP and swipe_start:
            swipe_end = pygame.mouse.get_pos()
            dx = swipe_end[0] - swipe_start[0]
            dy = swipe_end[1] - swipe_start[1]

            swipe_start = None

            # Detect swipe direction
            if abs(dx) > abs(dy) and abs(dx) > 20:
                if dx > 0:
                    dir_index = (dir_index + 1) % 4
                else:
                    dir_index = (dir_index - 1) % 4

                direction = directions[dir_index]

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Wall collision
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        game_over()

    # Self collision
    if new_head in snake:
        game_over()

    snake.insert(0, new_head)

    # Check if food expired
    if time.time() - food["spawn_time"] > food["type"]["lifetime"]:
        food = spawn_food()

    # am am am
    if new_head == food["pos"]:
        score += food["type"]["score"]
        foods_eaten += 1
        food = spawn_food()

        # Level up every 3 foods
        if foods_eaten % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    draw()
    clock.tick(speed)