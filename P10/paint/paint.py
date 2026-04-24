import pygame
import math

def main():
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    screen = pygame.display.set_mode((1080, 2180))
    clock = pygame.time.Clock()

    points = []
    radius = 8

    mode = "circle"   # draw / rect / circle / erase
    color = "green"

    start_pos = None

    screen.fill(BLACK)

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # KEYBOARD
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                # COLORS
                if event.key == pygame.K_1:
                    color = "red"
                elif event.key == pygame.K_2:
                    color = "green"
                elif event.key == pygame.K_3:
                    color = "blue"

                # MODES
                elif event.key == pygame.K_d:
                    mode = "draw"
                elif event.key == pygame.K_r:
                    mode = "rect"
                elif event.key == pygame.K_c:
                    mode = "circle"
                elif event.key == pygame.K_e:
                    mode = "erase"

            # MOUSE DOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos

                if mode == "draw":
                    points.append(event.pos)

                if mode == "erase":
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius * 2)

            # MOUSE MOTION
            if event.type == pygame.MOUSEMOTION:

                if mode == "draw" and pygame.mouse.get_pressed()[0]:
                    points.append(event.pos)

                if mode == "erase" and pygame.mouse.get_pressed()[0]:
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius * 2)

            # MOUSE UP (FIGURES)
            if event.type == pygame.MOUSEBUTTONUP and start_pos:

                end_pos = event.pos

                if mode == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos

                    rect = pygame.Rect(
                        min(x1, x2),
                        min(y1, y2),
                        abs(x2 - x1),
                        abs(y2 - y1)
                    )

                    pygame.draw.rect(screen, get_color(color), rect, 2)

                elif mode == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos

                    r = int(math.hypot(x2 - x1, y2 - y1))

                    pygame.draw.circle(screen, get_color(color), start_pos, r, 2)

                start_pos = None

        # DRAWING CANVAS LINES
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, color)
            i += 1

        pygame.display.flip()
        clock.tick(60)


def get_color(name):
    if name == "red":
        return (255, 0, 0)
    if name == "green":
        return (0, 255, 0)
    if name == "blue":
        return (0, 0, 255)
    return (255, 255, 255)


def drawLineBetween(screen, index, start, end, width, color_mode):

    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == "blue":
        color = (c1, c1, c2)
    elif color_mode == "red":
        color = (c2, c1, c1)
    elif color_mode == "green":
        color = (c1, c2, c1)
    else:
        color = (255, 255, 255)

    dx = start[0] - end[0]
    dy = start[1] - end[1]

    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return

    for i in range(steps):
        t = i / steps
        x = int((1 - t) * start[0] + t * end[0])
        y = int((1 - t) * start[1] + t * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


main()