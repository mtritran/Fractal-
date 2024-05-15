import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up screen
width, height = 640, 420
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fractal Tree")
clock = pygame.time.Clock()

# Set up variables
angle = 0
slider_value = math.pi / 4
len_slider_range = (0, math.pi * 2)
len_slider_step = 0.01
len_slider_pos = (50, height - 50)
len_slider_width = 200
dragging = False

# Function to draw the fractal tree
def branch(x, y, length, theta):
    x_end = x + length * math.sin(theta)
    y_end = y - length * math.cos(theta)
    pygame.draw.line(screen, (255, 255, 255), (x, y), (x_end, y_end), 2)

    if length > 4:
        branch(x_end, y_end, length * 0.67, theta + angle)
        branch(x_end, y_end, length * 0.67, theta - angle)     

# Function to save the image
def save_image(screen, filename):
    pygame.image.save(screen, filename)        

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    # Draw fractal tree
    angle = slider_value
    trunk_length = 100
    trunk_angle = 0
    trunk_end_x = width / 2
    trunk_end_y = height - trunk_length
    branch(trunk_end_x, trunk_end_y, trunk_length, trunk_angle)

    # Draw length slider
    len_slider_height = 10
    len_slider_pos = (width / 2 - len_slider_width / 2, height - 50)
    len_slider_rect = pygame.Rect(len_slider_pos[0], len_slider_pos[1], len_slider_width, len_slider_height)
    pygame.draw.rect(screen, (255, 255, 255), len_slider_rect, border_radius=5)

    # Calculate position of slider indicator
    slider_indicator_pos = len_slider_pos[0] + (slider_value / (math.pi * 2)) * len_slider_width

    # Draw slider indicator
    pygame.draw.circle(screen, (100, 100, 255), (int(slider_indicator_pos), len_slider_pos[1] + len_slider_height // 2), 8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len_slider_rect.collidepoint(event.pos):
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x = max(min(event.pos[0], len_slider_pos[0] + len_slider_width), len_slider_pos[0])
                slider_value = ((mouse_x - len_slider_pos[0]) / len_slider_width) * (math.pi * 2)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_image(screen, "Tree.png")   


    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
