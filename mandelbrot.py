import numpy as np
import pygame

# Define window size
width = 640
height = 360

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mandelbrot")

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def compute_mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_set = np.array([[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2])
    return (r1,r2,mandelbrot_set)

def display(xmin,xmax,ymin,ymax,width,height,max_iter):
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Mandelbrot Set')
    r1, r2, mandelbrot_set = compute_mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter)
    surface.fill((0,0,0))
    for y in range(len(r2)):
        for x in range(len(r1)):
            color = mandelbrot_set[y][x]
            surface.set_at((x, y), (color % 256, (color*5) % 256, (color*10) % 256))
    pygame.display.update()
    return surface

def save_image(screen, filename):
    pygame.image.save(screen, filename)

if __name__ == '__main__':
    WIDTH, HEIGHT = 800, 600
    MAX_ITER = 100
    XMIN, XMAX = -2.0, 1.0
    YMIN, YMAX = -1.5, 1.5
    pygame.init()
    screen = display(XMIN,XMAX,YMIN,YMAX,WIDTH,HEIGHT,MAX_ITER)

# Main loop
angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_image(screen, 'Mandelbrot.png')
