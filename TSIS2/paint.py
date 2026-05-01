import pygame
import math
import datetime
import time

def main():
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    screen = pygame.display.set_mode((1080, 2180))
    clock = pygame.time.Clock()

    radius = 8

    mode = "fill"   # draw / rect / circle / erase / square / right_triangle / equilateral_triangle / rhombus / line / fill / text
    color = "green"
    brush_size = 5 # 2 / 5 / 10
    
    font = pygame.font.SysFont(None, 40)
    typing = False
    text = ""
    text_pos = (0, 0)

    start_pos = None
    preview_end = None

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

                # SAVING
                if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                 filename = datetime.datetime.now().strftime("/storage/emulated/0/Download/drawing_%Y%m%d_%H%M%S.png")
                 pygame.image.save(screen, filename)
                 	
                # COLORS
                if event.key == pygame.K_q:
                    color = "red"
                elif event.key == pygame.K_w:
                    color = "green"
                elif event.key == pygame.K_e:
                    color = "blue"
                    
                 # SIZES
                if event.key == pygame.K_1:
                  brush_size = 2
                elif event.key == pygame.K_2:
                  brush_size = 5
                elif event.key == pygame.K_3:
                  brush_size = 10

                # MODES
                elif event.key == pygame.K_d:
                	mode = "draw"
                elif event.key == pygame.K_r:
                  mode = "rect"
                elif event.key == pygame.K_c:
                  mode = "circle"
                elif event.key == pygame.K_x:
                  mode = "erase"
                elif event.key == pygame.K_z:
                	mode = "square"
                elif event.key == pygame.K_t:
                	mode = "right_triangle"
                elif event.key == pygame.K_y:
                	mode = "equilateral_triangle"
                elif event.key == pygame.K_h:
                	mode = "rhombus"
                elif event.key == pygame.K_l:
                	mode = "line"
                elif event.key == pygame.K_f:
                	mode = "fill"
                elif event.key == pygame.K_p:
                	mode = "text"
                	
                # TEXT
                if typing:
                	if event.key == pygame.K_RETURN:
                		img = font.render(text, True, get_color(color))
                		screen.blit(img, text_pos)
                		typing = False
                	elif event.key == pygame.K_ESCAPE:
                		typing = False
                	elif event.key == pygame.K_BACKSPACE:
                		text = text[:-1]
                	else:
                		text += event.unicode

            # MOUSE DOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos

                if mode == "erase":
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius * 2)
                if mode == "text":
                	typing = True
                	text = ""
                	text_pos = event.pos
                if mode == "fill":
                	flood_fill(screen, event.pos[0], event.pos[1], get_color(color))
                	

            # MOUSE MOTION
            if event.type == pygame.MOUSEMOTION:

                if mode == "draw" and pygame.mouse.get_pressed()[0] and start_pos:
                   pygame.draw.line(screen, get_color(color), start_pos, event.pos, brush_size)
                   start_pos = event.pos

                if mode == "erase" and pygame.mouse.get_pressed()[0]:
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius * 2)
                if mode == "line" and start_pos:
                	preview_end = event.pos

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

                    pygame.draw.rect(screen, get_color(color), rect, brush_size)

                elif mode == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos

                    r = int(math.hypot(x2 - x1, y2 - y1))

                    pygame.draw.circle(screen, get_color(color), start_pos, r, brush_size)

                elif mode == "square":
                	x1, y1 = start_pos
                	x2, y2 = end_pos
                	side = min(abs(x2 - x1), abs(y2 - y1))
                	rect = pygame.Rect(x1, y1, 
                	side if x2 > x1 else -side,
                	side if y2 > y1 else -side)
                	pygame.draw.rect(screen, get_color(color), rect, brush_size)
                elif mode == "right_triangle":
                	x1, y1 = start_pos
                	x2, y2 = end_pos
                	points_triangle = [(x1, y1), (x2, y1), (x1, y2)]
                	pygame.draw.polygon(screen, get_color(color), points_triangle, brush_size)	
                elif mode == "equilateral_triangle":
                	x1, y1 = start_pos
                	x2, y2 = end_pos
                	
                	side = abs(x2 - x1)
                	height = int((math.sqrt(3) / 2) * side)
                	points_triangle = [(x1, y1), (x1 + side, y1), (x1 + side // 2, y1 - height)]
                	pygame.draw.polygon(screen, get_color(color), points_triangle, brush_size)
                elif mode == "rhombus":
                	x1, y1 = start_pos
                	x2, y2 = end_pos
                
                	cx = (x1 + x2) // 2
                	cy = (y1 + y2) // 2
                	
                	dx = abs(x2 - x1) // 2
                	dy = abs(y2 - y1) // 2
                	points_rhombus = [
                	(cx, y1),      # top
                	(x2, cy),      # right
                	(cx, y2),      # bottom
                	(x1, cy)       # left
                	]
                	pygame.draw.polygon(screen, get_color(color), points_rhombus, brush_size)
                
                elif mode == "line":
                	pygame.draw.line(screen, get_color(color), start_pos, end_pos, brush_size)
                
                start_pos = None

        temp_surface = screen.copy()
        if mode == "line" and start_pos and preview_end:
        	screen.blit(temp_surface, (0, 0))
        	pygame.draw.line(screen, get_color(color), start_pos, preview_end, 1)
        	
        if typing:
        	img = font.render(text, True, get_color(color))
        	screen.blit(img, text_pos)
        #if time.time() % 3 < 0.02: 
        #  pygame.image.save(screen, f"/storage/emulated/0/Download/drawing_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        pygame.display.flip()
        clock.tick(60)

def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))[:3]
    if target_color == new_color:
        return None
    stack = [(x, y)]
    while stack:
        px, py = stack.pop()
        if px < 0 or py < 0 or px >= surface.get_width() or py >= surface.get_height():
            continue
        if surface.get_at((px, py))[:3] != target_color:
            continue
        surface.set_at((px, py), new_color)

        stack.append((px+1, py))
        stack.append((px-1, py))
        stack.append((px, py+1))
        stack.append((px, py-1))


def get_color(name):
    if name == "red":
        return (255, 0, 0)
    if name == "green":
        return (0, 255, 0)
    if name == "blue":
        return (0, 0, 255)
    return (255, 255, 255)


main()