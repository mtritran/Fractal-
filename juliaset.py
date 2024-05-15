import math
import pygame

# Define window size
width = 640
height = 360

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Julia Set")

# Maximum number of iterations for each point on the complex plane
max_iterations = 100

# Colors to be used for each possible iteration count
colors_red = []
colors_green = []
colors_blue = []

# Create the colors to be used for each possible iteration count
for n in range(max_iterations):
    hu = math.sqrt(n / max_iterations)
    col = pygame.Color(0)
    col.hsla = (hu * 360, 100, 50, 100)
    colors_red.append(col.r)
    colors_green.append(col.g)
    colors_blue.append(col.b)

# Function to generate Julia Set
def generate_julia_set(ca, cb):
    # Create a surface for drawing
    surface = pygame.Surface((width, height))
    w = 5
    h = (w * height) / width
    xmin = -w / 2
    ymin = -h / 2
    xmax = xmin + w
    ymax = ymin + h

    # Calculate amount we increment x,y for each pixel
    dx = (xmax - xmin) / width
    dy = (ymax - ymin) / height

    # Start y
    y = ymin
    for j in range(height):
        # Start x
        x = xmin
        for i in range(width):
            # Now we test, as we iterate z = z^2 + cm does z tend towards infinity?
            a = x
            b = y
            n = 0
            while n < max_iterations:
                aa = a * a
                bb = b * b
                # Infinity in our finite world is simple, let's just consider it 16
                if aa + bb > 4.0:
                    break  # Bail
                twoab = 2.0 * a * b
                a = aa - bb + ca
                b = twoab + cb
                n += 1

            # We color each pixel based on how long it takes to get to infinity
            # If we never got there, let's pick the color black
            if n == max_iterations:
                surface.set_at((i, j), (0, 0, 0))
            else:
                # Otherwise, use the colors that we made in setup()
                surface.set_at((i, j), (colors_red[n], colors_green[n], colors_blue[n]))
            x += dx
        y += dy

    return surface

# Set up variables for slider
slider_width = 200
slider_height = 10
slider_pos = (width // 2 - slider_width // 2, height - 50)
slider_rect = pygame.Rect(slider_pos[0], slider_pos[1], slider_width, slider_height)
dragging = False

def save_image():
    pygame.image.save(screen, 'Julia.png')

# Main loop
angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if slider_rect.collidepoint(event.pos):
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x = max(min(event.pos[0], slider_pos[0] + slider_width), slider_pos[0])
                angle = ((mouse_x - slider_pos[0]) / slider_width) * 360
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_image()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Generate Julia Set based on the current angle
    ca = math.cos(math.radians(angle))
    cb = math.sin(math.radians(angle))
    julia_surface = generate_julia_set(ca, cb)

    # Blit the surface onto the screen
    screen.blit(julia_surface, (0, 0))

    # Draw slider
    pygame.draw.rect(screen, (255, 255, 255), slider_rect)

    # Draw slider indicator
    slider_indicator_pos = slider_pos[0] + (angle / 360) * slider_width
    pygame.draw.circle(screen, (255, 0, 0), (int(slider_indicator_pos), slider_pos[1] + slider_height // 2), 6)

    pygame.display.flip()

pygame.quit()
