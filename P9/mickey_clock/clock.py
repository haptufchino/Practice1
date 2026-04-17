import pygame
import datetime

def run():
    pygame.init()
    WIDTH, HEIGHT = 1075, 1220
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    bg = pygame.image.load("clock.png").convert()
    sec_img = pygame.image.load("lhand.png").convert_alpha()
    min_img = pygame.image.load("rhand.png").convert_alpha()
    CENTER = (WIDTH // 2, HEIGHT // 2)

    def rotate_hand(image, angle, center):
        w, h = image.get_size()
        rotated = pygame.transform.rotate(image, angle)
        pivot = pygame.math.Vector2(w / 2, h / 2)
        rotated_pivot = pivot.rotate(-angle)
        rect = rotated.get_rect()
        rect.center = (
            center[0] - rotated_pivot.x,
            center[1] - rotated_pivot.y
        )
        return rotated, rect

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        now = datetime.datetime.now()
        sec_angle = -now.second * 6 - 50
        min_angle = -now.minute * 6 - 36

        sec_surf, sec_rect = rotate_hand(sec_img, sec_angle, CENTER)
        min_surf, min_rect = rotate_hand(min_img, min_angle, CENTER)

        screen.blit(bg, (0, 0))
        screen.blit(sec_surf, sec_rect)
        screen.blit(min_surf, min_rect)
        pygame.display.flip()
        clock.tick(60)

run()