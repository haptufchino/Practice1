def run():
    import pygame
    
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((1080, 600))
    font = pygame.font.SysFont(None, 36)

    playlist = [
        "music/BIG SHOT.wav",
        "music/The Third Sanctuary.wav",
        "music/FRIEND INSIDE ME.wav",
        "music/yeaaaauuuuuuuuuuuuuuuuh.wav",
        "music/Green Goner.wav"
    ]

    index = 0

    def load_track(i):
        pygame.mixer.music.load(playlist[i])

    load_track(index)
    state = "play"
    start_pos = None
    swipe = 60
    green = (0, 255, 0)
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((1, 1, 1))
        pygame.draw.line(screen, green, (60, 20), (1020, 20), 5)
        pygame.draw.line(screen, green, (60, 20), (60, 480), 5)
        pygame.draw.line(screen, green, (60, 480), (1020, 480), 5)
        pygame.draw.line(screen, green, (1020, 20), (1020, 480), 5)
        screen.blit(font.render(" " * 50 + "Welcome to Music Player", True, (0, 255, 0)), (20, 150))
        screen.blit(font.render(" " * 40 + "Hope you find it very, very interesting", True, (0, 255, 0)), (20, 200))
        screen.blit(font.render(" " * 58 + playlist[index][6:], True, (255, 255, 255)), (20, 300))
        screen.blit(font.render(" " * 64 + state.upper(), True, (0, 255, 0)), (20, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos

            elif event.type == pygame.MOUSEBUTTONUP and start_pos:

                end_pos = event.pos
                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]

                if abs(dx) > swipe and dx < 0:
                    index = (index + 1) % len(playlist)
                    load_track(index)
                    pygame.mixer.music.play()
                    state = "playing"

                elif abs(dx) > swipe and dx > 0:
                    index = (index - 1) % len(playlist)
                    load_track(index)
                    pygame.mixer.music.play()
                    state = "playing"

                elif abs(dy) > swipe and dy < 0:
                    pygame.mixer.music.stop()
                    state = "stopped"

                else:
                    if state == "playing":
                        pygame.mixer.music.pause()
                        state = "paused"
                    elif state == "paused":
                        pygame.mixer.music.unpause()
                        state = "playing"
                    else:
                        pygame.mixer.music.play()
                        state = "playing"

                start_pos = None

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
   
run()