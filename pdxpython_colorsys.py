import colorsys
import pygame
from random import randint


def update_color(color, factor=.05, light=True):
    """
    Takes an RGB tuple color and returns the RGB tuple of a color that is
    <factor> steps lighter or darker.
    """
    r, g, b = [x / 255.0 for x in color]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    if light:
        l = l + factor
    else:
        l = l - factor
    rgb = [min(255, max(0, int(round(x * 255))))
           for x in colorsys.hls_to_rgb(h, l, s)]

    return (rgb[0], rgb[1], rgb[2])


def inset_box(rect, step=20):
    x, y, width, height = rect
    x += step
    y += step
    width -= (step * 2)
    height -= (step * 2)
    return (x, y, width, height)


color = (randint(0, 255), randint(0, 255), randint(0, 255))

pygame.init()
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PDX Python colorsys Demo")
done = False
clock = pygame.time.Clock()

screen.fill(color)

step = 0
rect = (20, 20, 660, 460)
light = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    clock.tick(20)
    step += 1
    if step < 10:
        color = update_color(color, light=light)
        pygame.draw.rect(screen, color, rect)
        rect = inset_box(rect) 
    else:
        light = not light
        pygame.time.wait(1000)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        step = 0
        rect = (20, 20, 660, 460)
        screen.fill(color)



    pygame.display.flip()

pygame.quit()
