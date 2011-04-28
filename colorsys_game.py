"""
Simply pygame app to display a handy use of colorsys
"""
import colorsys
import pygame
from random import randint

def font_color(bg):
    bg = tuple(x / 255.0 for x in bg)
    bg_hls = colorsys.rgb_to_hls(*bg)
    fg_hls = colorsys.hls_to_rgb(1, 1, 1)
    if fg_hls[1] > bg_hls[1]:
        light = fg_hls
        dark = bg_hls
    else:
        light = bg_hls
        dark = bg_hls
    
    ratio = (light[1] + .05) / (dark[1] + .05)

    if ratio >= (4.5 / 1):
        return (255, 255, 255)
    else:
        return (0, 0, 0)

color = (randint(0, 255), randint(0, 255), randint(0, 255)) 
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()
radius = randint(10, 50)
id = 0
circles = [{'x': 20,
            'y': randint(0, 500),
            'radius': radius,
            'speed': 15,
            'id': id,
            'color': color,
            'font_color': font_color(color)}]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    clock.tick(20)

    color = (randint(0, 255), randint(0, 255), randint(0, 255)) 
    screen.fill(black)
    
    new = False


    for ii, circ in enumerate(circles):
        pygame.draw.circle(screen, circ['color'], (circ['x'], circ['y']), circ['radius'])
        circ['x'] += circ['speed']
        if circ['x'] > 700 + radius:
            circ['x'] = -1 * radius
            new = True
        font = pygame.font.Font(None, circ['radius'])
        text = font.render(str(circ['id']), True, circ['font_color'])
        screen.blit(text, (circ['x'] - (circ['speed'] * 2), circ['y'] - circ['radius'] / 2))
    
    if new:
        id += 1
        circles.append({'x': randint(10, 200),
                        'y': randint(0, 500),
                        'radius': randint(10, 50),
                        'speed': randint(1, 20),
                        'id': id,
                        'color': color,
                        'font_color': font_color(color)})

    circles = circles[-100:] 
    pygame.display.flip()

pygame.quit()
