from turtle import Turtle, Screen
import pygame
from PIL import Image, ImageOps
import io

R = 1
L = 0

# Function to save the image
def save_image(screen, filename):
    pygame.image.save(screen, filename)

def dragon_curve(order):
    if order == 0:
        return [R]
    else:
        previous_curve = dragon_curve(order - 1)
        return previous_curve + [R] + [bit ^ 1 for bit in reversed(previous_curve)]

def draw_curve(curve, turtle, step_length, angle):
    for turn in curve:
        turtle.forward(step_length)
        turtle.right(angle if turn == R else -angle)

def main():
    # Turtle setup
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed("fastest")
    turtle.color("#ff69aa")

    # Pygame setup
    pygame.init()

    # Screen setup
    screen = Screen()
    screen.title("Dragon Curve")
    screen.bgcolor("black")
    screen.delay(0)

    # Position turtle at the start of the curve
    turtle.penup()
    turtle.goto(140, -90)
    turtle.pendown()

    # Draw Dragon Curve
    order = 12  # Adjust the order for different sizes
    curve = dragon_curve(order)
    draw_curve(curve, turtle, 5, 90)

    # Save the image
    image_data = screen.getcanvas().postscript(colormode='color')
    image = Image.open(io.BytesIO(image_data.encode('utf-8')))
    pygame_image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
    save_image(pygame_image, "DragonCurve.png")

    # Keep the window open until it is closed manually
    screen.mainloop()

if __name__ == "__main__":
    main()
