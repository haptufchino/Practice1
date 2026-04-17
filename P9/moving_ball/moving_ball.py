import pygame

def run():
    pygame.init()
    w, h = 1080, 2165
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    r = 25
    s = 20
    x, y = w // 2, h // 2
    dx, dy = 1, 0  

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                dx, dy = dy, -dx

        if pygame.mouse.get_pressed()[0]:
            new_x = x + dx * s
            new_y = y + dy * s

            if r <= new_x <= w - r:
                x = new_x
            else:
                if abs(new_x - r) < abs(new_x - w + r):
                    x = r
                else:
                    x = w - r

            if r <= new_y <= h - r:
                y = new_y
            else:
                if abs(new_y - r) < abs(new_y - h + r):
                    y = r
                else:
                    y = h - r

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), r)
        pygame.display.flip()
    pygame.quit()

run()